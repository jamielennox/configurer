import fixtures
import testtools

import configurer
from configurer.readers.environ import EnvironmentReader
from configurer.validators import Required


class SimpleComponent(configurer.Component):

    abc = configurer.Option('abc', parser=str)

    ghi = configurer.Option('ghi',
                            parser=str,
                            validator=[Required()])


class TestEnvironmentReader(testtools.TestCase):

    def environ_fixtures(self, **kwargs):
        for key, value in kwargs.items():
            self.useFixture(fixtures.EnvironmentVariable(key, value))

    def test_simple_read(self):
        cm = configurer.ConfigManager([EnvironmentReader()])
        comp = SimpleComponent(cm)
        self.environ_fixtures(ABC='hello world')
        self.assertEqual('hello world', comp.abc)

    def test_environ_prefix(self):
        cm = configurer.ConfigManager([EnvironmentReader(prefix='test')])
        comp = SimpleComponent(cm)
        self.environ_fixtures(TEST_ABC='hello world')
        self.assertEqual('hello world', comp.abc)

    def test_not_found(self):
        cm = configurer.ConfigManager([EnvironmentReader()])
        comp = SimpleComponent(cm)
        self.assertIs(configurer.NO_VALUE, comp.abc)

    def test_environ_required_property(self):
        cm = configurer.ConfigManager([EnvironmentReader()])
        comp = SimpleComponent(cm)

        with testtools.ExpectedException(configurer.ValidationError):
            comp.ghi
