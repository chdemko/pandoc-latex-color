# This Python file uses the following encoding: utf-8

from unittest import TestCase
from panflute import *

import pandoc_latex_color


def metadata():
    return {
        "pandoc-latex-color": MetaList(
            MetaMap(
                color=MetaString("red"),
                classes=MetaList(MetaString("class1"), MetaString("class2")),
            )
        )
    }


def opening(value, type):
    assert isinstance(value, type)
    assert value.format == "tex"
    assert value.text == "{\\color{red} "


def closing(value, type):
    assert isinstance(value, type)
    assert value.format == "tex"
    assert value.text == "}"


def span(elem, doc, color):
    pandoc_latex_color.main(doc)
    assert isinstance(elem.content[0], RawInline)
    assert elem.content[0].format == "tex"
    assert elem.content[0].text == "\\color{" + color + "} "


def test_span_classes():
    elem = Span(classes=["class1", "class2"])
    doc = Doc(Para(elem), metadata=metadata(), format="latex", api_version=(1, 17, 2))
    span(elem, doc, doc.get_metadata()["pandoc-latex-color"][0]["color"])


def test_span_attributes():
    elem = Span(attributes={"latex-color": "red"})
    doc = Doc(Para(elem), format="latex", api_version=(1, 17, 2))
    span(elem, doc, "red")


def div(elem, doc):
    pandoc_latex_color.main(doc)
    debug(elem.content)
    opening(elem.content[0], RawBlock)
    closing(elem.content[-1], RawBlock)


def test_div_classes():
    elem = Div(Para(Str("test")), classes=["class1", "class2"])
    doc = Doc(elem, metadata=metadata(), format="latex", api_version=(1, 17, 2))
    div(elem, doc)


def test_div_attributes():
    elem = Div(Para(Str("test")), attributes={"latex-color": "red"})
    doc = Doc(elem, format="latex", api_version=(1, 17, 2))
    div(elem, doc)


def test_div_multi():
    elem = Div(
        Para(Str("test")),
        BlockQuote(Para(Str("test"))),
        attributes={"latex-color": "red"},
    )
    doc = Doc(elem, format="latex", api_version=(1, 17, 2))
    div(elem, doc)


def test_bad_color():
    metadata = {
        "pandoc-latex-color": MetaList(
            MetaMap(
                color=MetaString("badcolor"),
                classes=MetaList(MetaString("class1"), MetaString("class2")),
            )
        )
    }
    elem = Span(classes=["class1", "class2"])
    doc = Doc(Para(elem), metadata=metadata, format="latex", api_version=(1, 17, 2))
    pandoc_latex_color.main(doc)
    assert isinstance(elem.content[0], RawInline)
    assert elem.content[0].format == "tex"
    assert elem.content[0].text == "\\color{black} "


def test_missing_color():
    metadata = {
        "pandoc-latex-color": MetaList(
            MetaMap(classes=MetaList(MetaString("class1"), MetaString("class2")))
        )
    }
    elem = Span(classes=["class1", "class2"])
    doc = Doc(Para(elem), metadata=metadata, format="latex", api_version=(1, 17, 2))
    span(elem, doc, "black")
