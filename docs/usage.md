Usage
=====

To apply the filter, use the following option with pandoc:

~~~shell-session
$ pandoc --filter pandoc-latex-color
~~~

Explanation
-----------

In the metadata block, specific set of classes can be defined to specify
the color for `span` elements.

The metadata block add information using the `pandoc-latex-color` entry
by a list of  definitions:

~~~markdown
pandoc-latex-color:
  - classes: [important]
    color: red
    bgcolor: blue
~~~

The metadata block above is used to set the color to `red` and
the background color to `blue` for `span` that have the `important`
class.

The specified colors must be a valid [X11 color name](https://www.w3.org/TR/css-color-3/#svg-color).

It's also possible to set a specific LaTeX color or a specific
background color using the `latex-color` or
the `latex-bgcolor` attributes.

Example
-------

Demonstration: Using [pandoc-latex-color-sample.txt] as input
gives output file in [pdf].

[pandoc-latex-color-sample.txt]: https://raw.githubusercontent.com/chdemko/pandoc-latex-color/develop/docs/images/pandoc-latex-color-sample.txt
[pdf]: https://raw.githubusercontent.com/chdemko/pandoc-latex-color/develop/docs/images/pandoc-latex-color-sample.pdf

