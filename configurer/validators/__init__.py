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
    """
    Base validator class.
    """

    allow_no_value = False

    def __call__(self, option, value):
        raise NotImplementedError()


class ValidatorGroup(Validator):

    allow_no_value = True

    def __init__(self, *validators):
        super(ValidatorGroup, self).__init__()
        self._validators = validators

    def chain(self, option, validator, value):
        """
        Call another validator from an existing validator.

        :param option: The option that is being processed.
        :type option: Option
        :param validator: The validator to call
        :type validator: Validator
        :param value: The value to pass to the validator.

        :raises ValidationError: When Validation fails for the value.
        """
        allow_no_value = getattr(validator, 'allow_no_value', False)

        if value is NO_VALUE and not allow_no_value:
            return

        validator(option, value)


class And(ValidatorGroup):
    """
    Validate that all attached validators pass the test.

    :param validators: The validators to assert against the value.
    :type validators: Validator
    """

    def __call__(self, option, value):
        for validator in self._validators:
            self.chain(option, validator, value)


class Or(ValidatorGroup):
    """
    Validate that any one of the attached validators pass the test.

    :param validators: The validators to assert against the value.
    :type validators: Validator
    """

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
    """
    Invert the validation result to assert the result.

    :param validators: The validators to assert against the value.
    :type validators: Validator
    """

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
    """
    Assert that the option is specified in the config values.
    """

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
    """
    Assert that the value matches a regular expression.

    :param pattern: The regular expression to test exists.
    :type pattern: str
    :param flags: flags to pass to the regular expression compilation.
    :type flags: int
    """

    def __init__(self, pattern, flags=0):
        super(Regex, self).__init__()
        self._value = re.compile(pattern, flags=flags)

    def __call__(self, option, value):
        if not self._value.match(value):
            m = "Value '%s' does not match regular expression '%s'. Got '%s'"
            raise ValidationError(m % (option.name,
                                       self._value.pattern,
                                       value))
