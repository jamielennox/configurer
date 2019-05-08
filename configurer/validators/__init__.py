import re

from configurer.consts import NO_VALUE
from configurer.exceptions import ValidationError


__all__ = [
    'Validator',
    'ValidatorGroup',

    'And',
    'Or',
    'Not',

    'Required',
    'GreaterThan',
    'LowerThan',

    'Regex',
]


class Validator(object):

    allow_no_value = False

    def __call__(self, option, value):
        raise NotImplementedError()


class ValidatorGroup(Validator):

    allow_no_value = True

    def __init__(self, *validators):
        super(ValidatorGroup, self).__init__()
        self._validators = validators

    def chain(self, option, validator, value):
        allow_no_value = getattr(validator, 'allow_no_value', False)

        if value is NO_VALUE and not allow_no_value:
            return

        validator(option, value)


class And(ValidatorGroup):

    def __call__(self, option, value):
        for validator in self._validators:
            self.chain(option, validator, value)


class Or(ValidatorGroup):

    def __call__(self, option, value):
        for validator in self._validators:
            try:
                self.chain(option, validator, value)
            except ValidationError:
                pass
            else:
                return

        raise ValidationError("No Or choice available")


class Not(ValidatorGroup):

    def __init__(self, *validators):
        if len(validators) != 1:
            raise ValueError("Not expects one validator")

        super(Not, self).__init__()

    def __call__(self, option, value):
        for validator in self._validators:
            try:
                self.chain(validator)
            except ValidationError:
                pass
            else:
                raise ValidationError("Not condition failed")


class Required(Validator):

    allow_no_value = True

    def __call__(self, option, value):
        if value is NO_VALUE:
            m = "Required value '%s' is unset" % option.name
            raise ValidationError(m)


class GreaterThan(Validator):

    def __init__(self, value):
        super(GreaterThan, self).__init__()
        self._value = value

    def __call__(self, option, value):
        if value < self._value:
            m = "Value '%s' should be greater than '%s'. Got '%s'"
            raise ValidationError(m % (option.name, self._value, value))


class LowerThan(Validator):

    def __init__(self, value):
        super(LowerThan, self).__init__()
        self._value = value

    def __call__(self, option, value):
        if value > self._value:
            m = "Value '%s' should be less than '%s'. Got '%s'"
            raise ValidationError(m % (option.name, self._value, value))


class Regex(Validator):

    def __init__(self, pattern, flags=0):
        super(Regex, self).__init__()
        self._value = re.compile(pattern, flags=flags)

    def __call__(self, option, value):
        if not self._value.match(value):
            m = "Value '%s' does not match regular expression '%s'. Got '%s'"
            raise ValidationError(m % (option.name,
                                       self._value.pattern,
                                       value))
