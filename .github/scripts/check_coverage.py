import json
from datetime import datetime
from itertools import groupby

from fastcore.script import call_parse
from ghapi.all import GhApi, context_github, github_token
from invoke import run

MAX_ANNOTATIONS = 50


class CheckRun:
    def __init__(self, owner, repo, pull=None):
        self.owner = owner
        self.repo = repo
        self.event = context_github.event
        self.api = GhApi(owner=owner, repo=repo, token=github_token())
        self.annotations = []
        try:
            self.pull = self.event.pull_request.number
        except AttributeError:
            self.pull = pull

    @property
    def head_sha(self):
        return self.api.pulls.get(self.pull).head.sha

    @property
    def pull_files(self):
        page = 1
        per_page = 100
        files = self.api.pulls.list_files(self.pull, page=page, per_page=per_page)
        while len(files) == per_page:
            page += 1
            files = self.api.pulls.list_files(self.pull, page=page, per_page=per_page)
        return files

    def main(self):
        now = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        files = ",".join(f["filename"] for f in self.pull_files)
        run(f"poetry run coverage json --include {files}")
        annotations = self.get_annotations()
        total_annotations = len(annotations)
        data = {
            "name": "Coverage Result",
            "head_sha": self.head_sha,
            "status": "completed",
            "conclusion": "failure" if total_annotations > 0 else "success",
            "completed_at": now,
            "output": {
                "title": "Coverage Result",
                "summary": f"Total annotations {total_annotations}",
                "text": "Coverage results",
                "annotations": annotations,
            },
        }
        self.api.checks.create(**data)

    def get_annotations(self):
        annotations = []
        with open("coverage.json") as coverage:
            cov = json.loads(coverage.read())
            for path, data in cov["files"].items():
                missing_lines = data["missing_lines"]
                if len(missing_lines) == 0:
                    continue
                for start, end in self.get_missing_range(missing_lines):
                    annotations.append(self.get_annotation(start, end, path))
                    if len(annotations) == MAX_ANNOTATIONS:
                        break
        return annotations

    def get_missing_range(self, range_list):
        for a, b in groupby(enumerate(range_list), lambda pair: pair[1] - pair[0]):
            b = list(b)
            yield b[0][1], b[-1][1]

    def get_annotation(self, start, end, path):
        return dict(
            path=path,
            start_line=start,
            end_line=end,
            annotation_level="warning",
            message=self.get_msg(start, end),
        )

    def get_msg(self, start, end):
        if start == end:
            return f"Line #L{start} not covered by tests"
        else:
            return f"Lines #L{start}-{end} not covered by tests"


@call_parse
def check_run(pull: int = None):
    CheckRun(owner="globophobe", repo="django-github-checks", pull=pull).main()
