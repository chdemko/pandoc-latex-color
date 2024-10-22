Installation
============

[![Python package](https://github.com/chdemko/pandoc-latex-color/workflows/Python%20package/badge.svg?branch=develop)](https://github.com/chdemko/pandoc-latex-color/actions/workflows/python-package.yml)
[![Hatch project](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://pypi.org/project/black/)
[![Coveralls](https://img.shields.io/coveralls/github/chdemko/pandoc-latex-color/develop.svg?logo=Codecov&logoColor=white)](https://coveralls.io/github/chdemko/pandoc-latex-color?branch=develop)
[![Scrutinizer](https://img.shields.io/scrutinizer/g/chdemko/pandoc-latex-color.svg?logo=scrutinizer)](https://scrutinizer-ci.com/g/chdemko/pandoc-latex-color/)
[![Code Climate](https://codeclimate.com/github/chdemko/pandoc-latex-color/badges/gpa.svg)](https://codeclimate.com/github/chdemko/pandoc-latex-color/)
[![CodeFactor](https://img.shields.io/codefactor/grade/github/chdemko/pandoc-latex-color/develop.svg?logo=codefactor)](https://www.codefactor.io/repository/github/chdemko/pandoc-latex-color)
[![Codacy](https://img.shields.io/codacy/grade/68aedbacd7a543cebe982966434f6d68.svg?logo=codacy)](https://app.codacy.com/gh/chdemko/pandoc-latex-color/dashboard)
[![PyPI version](https://img.shields.io/pypi/v/pandoc-latex-color.svg?logo=pypi&logoColor=white)](https://pypi.org/project/pandoc-latex-color/)
[![PyPI format](https://img.shields.io/pypi/format/pandoc-latex-color.svg?logo=pypi&logoColor=white)](https://pypi.org/project/pandoc-latex-color/)
[![License](https://img.shields.io/pypi/l/pandoc-latex-color.svg?logo=pypi&logoColor=white)](https://raw.githubusercontent.com/chdemko/pandoc-latex-color/develop/LICENSE)
[![Downloads](https://img.shields.io/pypi/dm/pandoc-latex-color?logo=pypi&logoColor=white)](https://pepy.tech/project/pandoc-latex-color)
[![Development Status](https://img.shields.io/pypi/status/pandoc-latex-color.svg?logo=pypi&logoColor=white)](https://pypi.org/project/pandoc-latex-color/)
[![Python version](https://img.shields.io/pypi/pyversions/pandoc-latex-color.svg?logo=Python&logoColor=white)](https://pypi.org/project/pandoc-latex-color/)
[![Pandoc version](https://img.shields.io/badge/pandoc-2.11%20|%202.12%20|%202.13%20|%202.14%20|%202.15%20|%202.16%20|%202.17%20|%202.18%20|%202.19%20|%203.0%20|%203.1%20|%203.2%20|%203.3%20|%203.4%20|%203.5-blue.svg?logo=markdown)](https://pandoc.org/)
[![Latest release](https://img.shields.io/github/release-date/chdemko/pandoc-latex-color.svg?logo=github)](https://github.com/chdemko/pandoc-latex-color/releases)
[![Last commit](https://img.shields.io/github/last-commit/chdemko/pandoc-latex-color/develop?logo=github)](https://github.com/chdemko/pandoc-latex-color/commit/develop/)
[![Repo Size](https://img.shields.io/github/repo-size/chdemko/pandoc-latex-color.svg?logo=github)](http://pandoc-latex-color.readthedocs.io/en/latest/)
[![Code Size](https://img.shields.io/github/languages/code-size/chdemko/pandoc-latex-color.svg?logo=github)](http://pandoc-latex-color.readthedocs.io/en/latest/)
[![Source Rank](https://img.shields.io/librariesio/sourcerank/pypi/pandoc-latex-color.svg?logo=libraries.io&logoColor=white)](https://libraries.io/pypi/pandoc-latex-color)
[![Docs](https://img.shields.io/readthedocs/pandoc-latex-color.svg?logo=read-the-docs&logoColor=white)](http://pandoc-latex-color.readthedocs.io/en/latest/)

*pandoc-latex-color* is a [pandoc] filter for setting the color to `Span`
that have speficied classes or `latex-color` attribute.

[pandoc]: http://pandoc.org/

Instructions
------------

*pandoc-latex-color* requires [python], a programming language that comes
pre-installed on linux and Mac OS X, and which is easily installed
[on Windows].

Install *pandoc-latex-color* using the bash command

~~~shell-session
$ pipx install pandoc-latex-color
~~~

To upgrade to the most recent release, use

~~~shell-session
$ pipx upgrade pandoc-latex-color
~~~

`pipx` is a script to install and run python applications in isolated
environments from the Python Package Index, [PyPI].
It can be installed using instructions given
[here](https://pipx.pypa.io/stable/).

It uses the *xcolor* LaTeX package to handle correctly colors in spans
and the *soulutf8* package for highlighing the text.

[python]: https://www.python.org
[on Windows]: https://www.python.org/downloads/windows
[PyPI]: https://pypi.org


Getting Help
------------

If you have any difficulties with *pandoc-latex-color*,
please feel welcome to [file an issue] on github so that we can help.

[file an issue]: https://github.com/chdemko/pandoc-latex-color/issues

Contribute
==========

Instructions
------------

Install `hatch`, then run

~~~shell-session
$ hatch run pip install pre-commit
$ hatch run pre-commit install
~~~

to install `pre-commit` before working on your changes.

Tests
-----

When your changes are ready, run

~~~shell-session
$ hatch test
$ hatch fmt --check
$ hatch run lint:check
$ hatch run docs:build
$ hatch build -t wheel
~~~

for running the tests, checking the style, building the documentation
and building the wheel.

