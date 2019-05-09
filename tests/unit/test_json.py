import testtools

import configurer
from configurer.readers import json
from configurer.validators import Required


class SimpleComponent(configurer.Component):

    abc = configurer.Option('abc', parser=str)

    ghi = configurer.Option('ghi',
                            parser=str,
                            validator=[Required()])


class TestYamlReader(testtools.TestCase):

    def test_simple_read(self):
        val = """
        {
            "test": {
                "abc": "hello",
                "ghi": "world"
            }
        }
        """

        cm = configurer.ConfigManager([json.StringReader(val)])
        comp = SimpleComponent(cm, ['test'])

        self.assertEqual('hello', comp.abc)
        self.assertEqual('world', comp.ghi)

    def test_more_nested_read(self):
        val = """
        {
            "test": {
                "that": {
                    "nesting": {
                        "works": {
                            "abc": "hello",
                            "ghi": "world"
                        }
                    }
                }
            }
        }
        """

        cm = configurer.ConfigManager([json.StringReader(val)])
        comp = SimpleComponent(cm, ['test', 'that', 'nesting', 'works'])

        self.assertEqual('hello', comp.abc)
        self.assertEqual('world', comp.ghi)
