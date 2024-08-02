from unittest import TestCase
from panflute import (
    Doc,
    convert_text,
)

import pandoc_latex_color


class ColorTestCase(TestCase):
    @classmethod
    def conversion(cls, markdown) -> Doc:
        """
        Convert a markdown text to a panflute instance.

        Parameters
        ----------
        markdown
            Text

        Returns
        -------
        Doc
            A panflute document
        """
        doc = convert_text(markdown, standalone=True)
        doc.format = "latex"
        pandoc_latex_color.main(doc)
        return doc

    def verify_conversion(self, markdown, expected, output_format="latex") -> None:
        """
        Verify the conversion

        Parameters
        ----------
        markdown
            Input text
        expected
            Expected output
        output_format
            Desired conversion
        """
        doc = self.conversion(markdown)
        text = convert_text(
            doc,
            input_format="panflute",
            output_format=output_format,
            extra_args=["--wrap=none"],
        )
        print(text.strip())
        print(expected.strip())
        self.assertEqual(text.strip(), expected.strip())

    def test_span_classes(self):
        self.verify_conversion(
            """
---
pandoc-latex-color:
  - classes: [class1, class2]
    color: red
---

[This is a span]{.class1 .class2}
            """,
            """
{\\color{red}This is a span}
            """,
        )
        self.verify_conversion(
            """
---
pandoc-latex-color:
  - classes: [class1, class2]
    color: red
    bgcolor: blue
---

[**This is a span**]{.class1 .class2}
            """,
            """
{\\color{red}\\sethlcolor{blue}\\hl{\\textbf{This is a span}}}
            """,
        )

        def test_span_attributes(self):
            self.verify_conversion(
                """
    [This is a span]{latex-color="red"}
                """,
                """
    {\\color{red}This is a span}
                """,
            )
            self.verify_conversion(
                """
    [This is a span]{latex-color="red" latex-bgcolor="blue"}
                """,
                """
    {\\color{red}\\sethlcolor{blue}\\hl{This is a span}}
                """,
            )

    def test_bad_color(self):
        self.verify_conversion(
            """
[This is a span]{latex-color="badcolor"}
            """,
            """
{\\color{black}This is a span}
            """,
        )

    def test_missing_color(self):
        self.verify_conversion(
            """
---
pandoc-latex-color:
  - classes: [class1, class2]
---

[This is a span]{.class1 .class2}
            """,
            """
{\\color{black}This is a span}
            """,
        )
