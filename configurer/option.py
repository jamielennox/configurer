from configurer.consts import NO_VALUE
from configurer.validators import And


class Option(object):

    def __init__(self,
                 name,
                 parser=None,
                 validator=None,
                 default=NO_VALUE,
                 doc=None):
        self._name = name
        self._parser = parser
        self._default = default
        self._validator = And(*(validator or []))
        self._doc = doc

    def parse(self, value):
        if value is NO_VALUE:
            return NO_VALUE

        if self._parser:
            return self._parser(value)

        return value

    def validate(self, value):
        self._validator(self, value)

    def __get__(self, obj, objtype=None):
        value = obj.get(self._name)

        if value is NO_VALUE:
            value = self._default

        value = self.parse(value)
        self.validate(value)
        return value

    def __repr__(self):
        return '<Option(%s)>' % self._name
