#!/usr/bin/env python

"""
Pandoc filter for changing color in LaTeX.
"""
from __future__ import annotations

from typing import Any

from panflute import (
    Doc,
    Element,
    MetaInlines,
    MetaList,
    RawInline,
    Span,
    debug,
    run_filter,
)


def x11colors() -> dict[str, str]:
    """
    Get the x1 colors.

    Returns
    -------
    dict[str, str]
        A dictionary of colornames -> colorcode.
    """
    # See https://www.w3.org/TR/css-color-3/#svg-color
    return {
        "aliceblue": "F0F8FF",
        "antiquewhite": "FAEBD7",
        "aqua": "00FFFF",
        "aquamarine": "7FFFD4",
        "azure": "F0FFFF",
        "beige": "F5F5DC",
        "bisque": "FFE4C4",
        "black": "000000",
        "blanchedalmond": "FFEBCD",
        "blue": "0000FF",
        "blueviolet": "8A2BE2",
        "brown": "A52A2A",
        "burlywood": "DEB887",
        "cadetblue": "5F9EA0",
        "chartreuse": "7FFF00",
        "chocolate": "D2691E",
        "coral": "FF7F50",
        "cornflowerblue": "6495ED",
        "cornsilk": "FFF8DC",
        "crimson": "DC143C",
        "cyan": "00FFFF",
        "darkblue": "00008B",
        "darkcyan": "008B8B",
        "darkgoldenrod": "B8860B",
        "darkgray": "A9A9A9",
        "darkgreen": "006400",
        "darkgrey": "A9A9A9",
        "darkkhaki": "BDB76B",
        "darkmagenta": "8B008B",
        "darkolivegreen": "556B2F",
        "darkorange": "FF8C00",
        "darkorchid": "9932CC",
        "darkred": "8B0000",
        "darksalmon": "E9967A",
        "darkseagreen": "8FBC8F",
        "darkslateblue": "483D8B",
        "darkslategray": "2F4F4F",
        "darkslategrey": "2F4F4F",
        "darkturquoise": "00CED1",
        "darkviolet": "9400D3",
        "deeppink": "FF1493",
        "deepskyblue": "00BFFF",
        "dimgray": "696969",
        "dimgrey": "696969",
        "dodgerblue": "1E90FF",
        "firebrick": "B22222",
        "floralwhite": "FFFAF0",
        "forestgreen": "228B22",
        "fuchsia": "FF00FF",
        "gainsboro": "DCDCDC",
        "ghostwhite": "F8F8FF",
        "gold": "FFD700",
        "goldenrod": "DAA520",
        "gray": "808080",
        "green": "008000",
        "greenyellow": "ADFF2F",
        "grey": "808080",
        "honeydew": "F0FFF0",
        "hotpink": "FF69B4",
        "indianred": "CD5C5C",
        "indigo": "4B0082",
        "ivory": "FFFFF0",
        "khaki": "F0E68C",
        "lavender": "E6E6FA",
        "lavenderblush": "FFF0F5",
        "lawngreen": "7CFC00",
        "lemonchiffon": "FFFACD",
        "lightblue": "ADD8E6",
        "lightcoral": "F08080",
        "lightcyan": "E0FFFF",
        "lightgoldenrodyellow": "FAFAD2",
        "lightgray": "D3D3D3",
        "lightgreen": "90EE90",
        "lightgrey": "D3D3D3",
        "lightpink": "FFB6C1",
        "lightsalmon": "FFA07A",
        "lightseagreen": "20B2AA",
        "lightskyblue": "87CEFA",
        "lightslategray": "778899",
        "lightslategrey": "778899",
        "lightsteelblue": "B0C4DE",
        "lightyellow": "FFFFE0",
        "lime": "00FF00",
        "limegreen": "32CD32",
        "linen": "FAF0E6",
        "magenta": "FF00FF",
        "maroon": "800000",
        "mediumaquamarine": "66CDAA",
        "mediumblue": "0000CD",
        "mediumorchid": "BA55D3",
        "mediumpurple": "9370DB",
        "mediumseagreen": "3CB371",
        "mediumslateblue": "7B68EE",
        "mediumspringgreen": "00FA9A",
        "mediumturquoise": "48D1CC",
        "mediumvioletred": "C71585",
        "midnightblue": "191970",
        "mintcream": "F5FFFA",
        "mistyrose": "FFE4E1",
        "moccasin": "FFE4B5",
        "navajowhite": "FFDEAD",
        "navy": "000080",
        "oldlace": "FDF5E6",
        "olive": "808000",
        "olivedrab": "6B8E23",
        "orange": "FFA500",
        "orangered": "FF4500",
        "orchid": "DA70D6",
        "palegoldenrod": "EEE8AA",
        "palegreen": "98FB98",
        "paleturquoise": "AFEEEE",
        "palevioletred": "DB7093",
        "papayawhip": "FFEFD5",
        "peachpuff": "FFDAB9",
        "peru": "CD853F",
        "pink": "FFC0CB",
        "plum": "DDA0DD",
        "powderblue": "B0E0E6",
        "purple": "800080",
        "red": "FF0000",
        "rosybrown": "BC8F8F",
        "royalblue": "4169E1",
        "saddlebrown": "8B4513",
        "salmon": "FA8072",
        "sandybrown": "F4A460",
        "seagreen": "2E8B57",
        "seashell": "FFF5EE",
        "sienna": "A0522D",
        "silver": "C0C0C0",
        "skyblue": "87CEEB",
        "slateblue": "6A5ACD",
        "slategray": "708090",
        "slategrey": "708090",
        "snow": "FFFAFA",
        "springgreen": "00FF7F",
        "steelblue": "4682B4",
        "tan": "D2B48C",
        "teal": "008080",
        "thistle": "D8BFD8",
        "tomato": "FF6347",
        "turquoise": "40E0D0",
        "violet": "EE82EE",
        "wheat": "F5DEB3",
        "white": "FFFFFF",
        "whitesmoke": "F5F5F5",
        "yellow": "FFFF00",
        "yellowgreen": "9ACD32",
    }


def color_code(color: str | bool) -> str:
    """
    Get the LaTeX color code.

    Arguments
    ---------
    color
        X11 color name

    Returns
    -------
    str
        The LaTeX color code.
    """
    if color:
        return f"\\color{{{color}}}"
    return "\\color{black}"


def bgcolor_code(color: str | bool) -> str | bool:
    """
    Get the LaTeX color code for the background.

    Arguments
    ---------
    color
        X11 color name

    Returns
    -------
    str | bool
        The LaTeX color code for the background.
    """
    if color:
        return f"\\sethlcolor{{{color}}}"
    return False


def get_correct_color(color: str | bool) -> str | bool:
    """
    Get a correct color name.

    Arguments
    ---------
    color
        Color name

    Returns
    -------
    str | bool
        A X11 color name or False.
    """
    if color in x11colors():
        return color
    if color:
        debug(
            f"[WARNING] pandoc-latex-color: {color}"
            f" is not a correct X11 color; using black"
        )
        return "black"
    return False


def add_latex(elem: Element, color: str | bool, bgcolor: str | bool) -> None:
    """
    Insert LaTeX code.

    Arguments
    ---------
    elem
        The pandoc element
    color
        The X11 color name
    bgcolor
        The X11 bgcolor name
    """
    elem.content.insert(0, RawInline(color, "tex"))
    if isinstance(bgcolor, str):
        elem.content.insert(1, RawInline(f"{bgcolor}\\hl{{", "tex"))
        elem.content.append(RawInline("}", "tex"))


def colorize(elem: Element, doc: Doc) -> None:
    """
    Colorize an element.

    Arguments
    ---------
    elem
        The pandoc element
    doc
        The pandoc document
    """
    # Is it in the right format and is it a Span ?
    if doc.format in ("latex", "beamer") and isinstance(elem, Span):
        # Is there a latex-color attribute?
        if "latex-color" in elem.attributes or "latex-bgcolor" in elem.attributes:
            try:
                color = elem.attributes["latex-color"]
            except KeyError:
                color = "black"

            try:
                bgcolor = elem.attributes["latex-bgcolor"]
            except KeyError:
                bgcolor = False

            add_latex(
                elem,
                color_code(get_correct_color(color)),
                bgcolor_code(get_correct_color(bgcolor)),
            )
            return

        # Get the classes
        classes = set(elem.classes)

        # Loop on all color definition
        for definition in doc.defined:
            # Are the classes correct?
            if classes >= definition["classes"]:
                add_latex(elem, definition["color"], definition["bgcolor"])
                return


def prepare(doc: Doc) -> None:
    """
    Prepare the document.

    Arguments
    ---------
    doc
        The pandoc document
    """
    # Prepare the definitions
    doc.defined = []

    # Get the meta data
    meta = doc.get_metadata("pandoc-latex-color")

    if isinstance(meta, list):
        # Loop on all definitions
        for definition in meta:
            # Verify the definition
            if (
                isinstance(definition, dict)
                and "classes" in definition
                and isinstance(definition["classes"], list)
            ):
                add_definition(doc.defined, definition)


def add_definition(defined: list[dict[str, Any]], definition: dict[str, Any]) -> None:
    """
    Add a definition.

    Arguments
    ---------
    defined
        A list of definition
    definition
        A new definition
    """
    # Get the classes
    classes = definition["classes"]

    # Get the color
    if "color" in definition:
        color = get_correct_color(definition["color"])
    else:
        color = "black"

    # Get the bgcolor
    if "bgcolor" in definition:
        bgcolor = get_correct_color(definition["bgcolor"])
    else:
        bgcolor = False

    # Add a definition
    defined.append(
        {
            "classes": set(classes),
            "color": color_code(color),
            "bgcolor": bgcolor_code(bgcolor),
        }
    )


def finalize(doc: Doc) -> None:
    """
    Finalize the document.

    Arguments
    ---------
    doc
        The pandoc document
    """
    # Add header-includes if necessary
    if "header-includes" not in doc.metadata:
        doc.metadata["header-includes"] = MetaList()
    # Convert header-includes to MetaList if necessary
    elif not isinstance(doc.metadata["header-includes"], MetaList):
        doc.metadata["header-includes"] = MetaList(doc.metadata["header-includes"])

    # Add useful LaTexPackage
    doc.metadata["header-includes"].append(
        MetaInlines(RawInline("\\usepackage{xcolor}", "tex"))
    )
    doc.metadata["header-includes"].append(
        MetaInlines(RawInline("\\usepackage{soulutf8,color}", "tex"))
    )
    doc.metadata["header-includes"].append(
        MetaInlines(RawInline("\\soulregister\\cite7", "tex"))
    )
    doc.metadata["header-includes"].append(
        MetaInlines(RawInline("\\soulregister\\ref7", "tex"))
    )
    doc.metadata["header-includes"].append(
        MetaInlines(RawInline("\\soulregister\\pageref7", "tex"))
    )

    for color, value in x11colors().items():
        doc.metadata["header-includes"].append(
            MetaInlines(
                RawInline(f"\\definecolor{{{color}}}{{HTML}}{{{value}}}", "tex")
            )
        )

    if doc.format == "beamer":
        special_beamer = [
            "\\makeatletter",
            "\\let\\HL\\hl",
            "\\renewcommand\\hl{%",
            "\\let\\set@color\\beamerorig@set@color",
            "\\let\\reset@color\\beamerorig@reset@color",
            "\\HL}",
            "\\makeatother",
        ]
        for line in special_beamer:
            doc.metadata["header-includes"].append(MetaInlines(RawInline(line, "tex")))


def main(doc: Doc | None = None) -> Doc:
    """
    Convert the pandoc document.

    Arguments
    ---------
    doc
        The pandoc document

    Returns
    -------
    Doc
        The modified pandoc document
    """
    return run_filter(colorize, prepare=prepare, finalize=finalize, doc=doc)


if __name__ == "__main__":
    main()
