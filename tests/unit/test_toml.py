import testtools

import configurer
from configurer.ext import toml
from configurer.validators import Required


class SimpleComponent(configurer.Component):

    abc = configurer.Option('abc', parser=str)

    ghi = configurer.Option('ghi',
                            parser=str,
                            validator=[Required()])


class TesttomlReader(testtools.TestCase):

    def test_simple_read(self):
        val = """
        [test]
        abc = "hello"
        ghi = "world"
        """

        cm = configurer.ConfigManager([toml.StringReader(val)])
        comp = SimpleComponent(cm, ['test'])

        self.assertEqual('hello', comp.abc)
        self.assertEqual('world', comp.ghi)

    def test_more_nested_read(self):
        val = """
        [test]
            [test.that]
                [test.that.nesting]
                    [test.that.nesting.works]
                        abc = "hello"
                        ghi = "world"
        """

        cm = configurer.ConfigManager([toml.StringReader(val)])
        comp = SimpleComponent(cm, ['test', 'that', 'nesting', 'works'])

        self.assertEqual('hello', comp.abc)
        self.assertEqual('world', comp.ghi)
