from configurer.consts import NO_VALUE
from configurer.validators import And


class Option(object):
    """
    A defined configuration option.

    :param name: The name of the option that will be looked up.
    :type name: str
    :param parser: Function to parse the config value.
    :param default: A default value to return if not found.
    :param validator: Validation functions to run on the returned config value.
    :param doc: An explanatory string to add to any documentation.
    :type doc: str, Optional
    """

    def __init__(self,
                 name,  # type: str
                 parser=None,  # type: Optional[Callable[[Any], Any]]
                 validator=None,
                 default=NO_VALUE,  # type: Optional[Any]
                 doc=None,  # type: Optional[str]
                 ):
        self._name = name
        self._parser = parser
        self._default = default
        self._validator = And(*(validator or []))
        self._doc = doc

    @property
    def name(self):
        """
        The option identifier for the Option.

        :returns: The name of the Option
        :rtype: str
        """
        return self._name

    def parse(self, value):
        """
        Parse a value that will be returned according to the option spec.

        :param value: The value returned by the config option pool.
        :returns: The value that should be returned to the config pool.
        """
        if value is NO_VALUE:
            return NO_VALUE

        if self._parser:
            return self._parser(value)

        return value

    def validate(self, value):
        """
        Validate a value against the validators stored in the Option.

        :param value: The value that should be validated.

        :raises configurer.ValidationError: On validation failure.
        """
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
