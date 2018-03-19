# pandoc-latex-color
[![Build Status](https://img.shields.io/travis/chdemko/pandoc-latex-color/0.0.1.svg)](https://travis-ci.org/chdemko/pandoc-latex-color/branches)
[![Coveralls](https://img.shields.io/coveralls/github/chdemko/pandoc-latex-color/0.0.1.svg)](https://coveralls.io/github/chdemko/pandoc-latex-color?branch=0.0.1)
[![Scrutinizer](https://img.shields.io/scrutinizer/g/chdemko/pandoc-latex-color.svg)](https://scrutinizer-ci.com/g/chdemko/pandoc-latex-color/)
[![PyPI version](https://img.shields.io/pypi/v/pandoc-latex-color.svg)](https://pypi.org/project/pandoc-latex-color/)
[![PyPI format](https://img.shields.io/pypi/format/pandoc-latex-color.svg)](https://pypi.org/project/pandoc-latex-color/)
[![License](https://img.shields.io/pypi/l/pandoc-latex-color/0.0.1.svg)](https://raw.githubusercontent.com/chdemko/pandoc-latex-color/0.0.1/LICENSE)
[![Downloads](https://img.shields.io/pypi/dm/pandoc-latex-color.svg)](https://pypi.org/project/pandoc-latex-color/)
[![Python version](https://img.shields.io/pypi/pyversions/pandoc-latex-color/0.0.1.svg)](https://pypi.org/project/pandoc-latex-color/0.0.1/)
[![Development Status](https://img.shields.io/pypi/status/pandoc-latex-color/0.0.1.svg)](https://pypi.org/project/pandoc-latex-color/0.0.1/)

*pandoc-latex-color* is a [pandoc] filter for setting the color to `Span`, and `Div` that have speficied classes or `latex-color` attribute.

[pandoc]: http://pandoc.org/

Documentation
-------------

See the [wiki pages](https://github.com/chdemko/pandoc-latex-color/wiki).

Usage
-----

To apply the filter, use the following option with pandoc:

    --filter pandoc-latex-color

Installation
------------

*pandoc-latex-color* requires [python], a programming language that comes pre-installed on linux and Mac OS X, and which is easily installed [on Windows]. Either python 2.7 or 3.x will do.

Install *pandoc-latex-color* as root using the bash command

    pip install pandoc-latex-color

To upgrade to the most recent release, use

    pip install --upgrade pandoc-latex-color

`pip` is a script that downloads and installs modules from the Python Package Index, [PyPI].  It should come installed with your python distribution. If you are running linux, `pip` may be bundled separately. On a Debian-based system (including Ubuntu), you can install it as root using

    apt-get update
    apt-get install python-pip

It uses the *xcolor* LaTeX package to handle correctly colors in spans and divs.

[python]: https://www.python.org
[on Windows]: https://www.python.org/downloads/windows
[PyPI]: https://pypi.org


Getting Help
------------

If you have any difficulties with *pandoc-latex-color*, please feel welcome to [file an issue] on github so that we can help.

[file an issue]: https://github.com/chdemko/pandoc-latex-color/issues

