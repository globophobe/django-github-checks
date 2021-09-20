---
theme: ./
---

# How to make yourself unpopular

自分は人気ではないにする方法

`Using the GitHub API`

---

# These slides are at Connpass. So you can check them out.

スライドはConnpassにアップされています。 是非みてください。

---

# Who am I?

お前誰?

---

# My name is Alex, and I'm from Canada 🇨🇦

アレックスです。カナダから来ました。

---
layout: image-right
image: ./assets/arex.jpg
href: https://github.com/globophobe
maxWidth: 80%
caption: globophobe 
---

# My username on Connpass is globophobe.

Connpassのユーザ名はglobophobeです。

---

# I write code with Django and Vue.js at <a href="https://creditengine.jp/"><img class="inline" style="height: 4rem;" src="/assets/credit-engine.svg" alt="Credit Engine" /></a>.

<a href="https://creditengine.jp/">クレジットエンジン</a>のエンジニアとして、DjangoとVue.jsを利用してプログラミングをしています。

---

# Recently, I have been interested in the GitHub API.

最近、GitHubAPIにハマっています。

---

# It seems the [checks API](https://docs.github.com/en/rest/reference/checks) allows annotating pull requests.

チェックAPIを使って、プルリクに注釈を付けること出来るだそうです。

---

# TLDR; I tried it with this repo: 

このリポジトリで試してみました：

# [pythontokai-gitub-checks](https://github.com/globophobe/pythontokai-github-checks)

---

# This is the result:

その結果は：

<img src="/assets/failing-coverage.png" />

---

# There is a line of code with no coverage, so the check failed:

カバレッジがない行があるので、失敗しました。

<img src="/assets/failing-coverage-annotation.png" />

---

# How does it work?

どうやって？

---
layout: code
text: "The repo has a GitHub workflow, which does the following for pull requests:"
trans: リポにはワークフローがあります。プルリクに対して次のことを行います：
---

1. `poetry run coverage run github_checks/manage.py test`
2. `poetry run python .github/scripts/check_coverage.py`

---
layout: code
text: "The logic is contained in <code>check_coverage.py</code>:"
trans: そのロジックは：
---

1. Use the GitHub API to get list of files for the pull request.
   * GitHub APIを使用して、プルリクエストのファイルのリストを取得します。
2. Use the GitHub API to annotate the pull request.
   * GitHub APIを使用して、プルリクエストに注釈を付けます。

---

# To be honest<p class="ellipsis">...</p>

正直に。。。

---

# I don't enjoy writing shell commands.

シェルコマンドを書くのはあまり好きではありません。

---
layout: code
text: "<code>check_coverage.py</code> was written with 3 great Python packages."
trans: 3つの素晴らしいPythonパッケージでを利用して書けられました。
---

1. [ghapi](https://github.com/fastai/ghapi)
2. [fastcore](https://github.com/fastai/fastcore)
3. [invoke](https://github.com/pyinvoke/invoke)

---

# [ghapi](https://github.com/fastai/ghapi) makes it easy to use the GitHub API with Python.
ghapiを使用すると、PythonでGitHubAPIを簡単に使用出来ます。

---

# [fastcore](https://github.com/fastai/fastcore) is a dependency of ghapi, and has some interesting methods.

fastcoreはghapiの依存関係で、いくつかの興味深いメソッドがあります。

---

# [invoke](https://github.com/pyinvoke/invoke) makes it easy to call shell commands with Python.

invokeを使用すると、Pythonでシェルコマンドを簡単に呼び出す事が出来ます。

---

# ...

---

# That's all thanks for listening!

以上です。ご清聴ありがとうございます。
