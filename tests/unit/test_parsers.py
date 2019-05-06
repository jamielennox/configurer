import testtools

from configurer import parsers


class TestBoolean(testtools.TestCase):

    def bool(self, value):
        return parsers.boolean(value)

    def test_bool_types(self):
        self.assertIs(True, self.bool(True))
        self.assertIs(False, self.bool(False))
