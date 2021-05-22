from collections import OrderedDict

from hamcrest import equal_to, assert_that

from serializer import Serializable


class AttributesTestClass(Serializable):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.a = {'@href': 'x', '@class': 'z', '#text': 'y'}


def test_to_xml_attributes():
    tac = AttributesTestClass()
    expected_xml = '''<?xml version="1.0" encoding="utf-8"?>\n<NewClass>\n\t<a class="z" href="x">y</a>\n</NewClass>\n'''
    assert_that(tac.to_xml(pretty_print=True, custom_root='NewClass'), equal_to(expected_xml))


def test_from_xml_attributes():
    tac = AttributesTestClass()
    source_xml = '''<?xml version="1.0" encoding="utf8"?><AttributesTestClass><a class="z" href="x">y</a>
    <a class="n" href="m">h</a></AttributesTestClass>'''
    assert_that(tac.from_xml(source_xml).a, equal_to([OrderedDict([('@class', 'z'), ('@href', 'x'), ('#text', 'y')]),
                                                      OrderedDict([('@class', 'n'), ('@href', 'm'), ('#text', 'h')])]))


def test_namespace_to_xml():
    tac = AttributesTestClass()
    expected_xml = '''<?xml version="1.0" encoding="utf-8"?><AttributesTestClass xmlns="https://ssl.com/PV"><a class="z" href="x">y</a></AttributesTestClass>'''
    assert_that(tac.to_xml(pretty_print=False, namespace='https://ssl.com/PV'), equal_to(expected_xml))


def test_no_header_pretty_print_to_xml():
    tac = AttributesTestClass()
    expected_xml = '''<AttributesTestClass>\n\t<a class="z" href="x">y</a>\n</AttributesTestClass>\n'''
    assert_that(tac.to_xml(pretty_print=True, no_header=True), equal_to(expected_xml))


def test_no_header_normal_print_to_xml():
    tac = AttributesTestClass()
    expected_xml = '''<AttributesTestClass><a class="z" href="x">y</a></AttributesTestClass>'''
    assert_that(tac.to_xml(pretty_print=False, no_header=True), equal_to(expected_xml))


def test_to_json():
    tac = AttributesTestClass()
    expected_json = '{"a": {"@href": "x", "@class": "z", "#text": "y"}}'
    assert_that(tac.to_json(pretty_print=False), equal_to(expected_json))


def test_from_json():
    tac = AttributesTestClass()
    source_json = '''{
  "a": {
    "@href": "n",
    "@class": "m",
    "#text": "h"
  }
}'''
    tac.from_json(source_json)
    assert_that(tac.to_json(), equal_to(source_json))
