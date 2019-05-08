import testtools

from configurer.exceptions import ValidationError
from configurer import option
from configurer import validators

o = option.Option('test_option')


class TestRegexValidator(testtools.TestCase):

    def test_some_examples(self):
        r = validators.Regex("^abc")

        r(o, "abcdef")
        self.assertRaises(ValidationError, r, o, "xyz")
