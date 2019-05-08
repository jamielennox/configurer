import testtools

from configurer import parsers


class TestBooleanParser(testtools.TestCase):

    def bool(self, value):
        return parsers.Boolean(value)

    def test_bool_types(self):
        self.assertIs(True, self.bool(True))
        self.assertIs(False, self.bool(False))

    def test_str_true_values(self):
        for val in ('true',
                    'TrUE ',
                    'YES',
                    'yes',
                    'on',
                    ' oN'):
            self.assertIs(True, self.bool(val))

    def test_str_false_values(self):
        for val in ('false',
                    'FALse ',
                    'No',
                    'ofF',
                    '0   ',
                    'no',
                    ):
            self.assertIs(False, self.bool(val))

    def test_unknown_values(self):
        for val in ('bad',
                    'none',
                    None):
            self.assertRaises(ValueError, self.bool, val)


class TestListParser(testtools.TestCase):

    def test_list_str(self):
        self.assertEqual(['abc', 'def', 'ghi'],
                         parsers.List(str)("abc,def,ghi"))


class TestOrParser(testtools.TestCase):

    def test_parse_int_or_str(self):
        self.assertEqual(12, parsers.Or(int)('12'))
        self.assertEqual(12, parsers.Or(int, str)('12'))
        self.assertEqual('12', parsers.Or(str, int)('12'))

    def test_parse_int_or_bool(self):
        p = parsers.List(parsers.Or(parsers.Boolean, int, str))
        self.assertEqual([True, 11, 'def'], p("Yes,11,def"))
