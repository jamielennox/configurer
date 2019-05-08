from configurer.consts import NO_VALUE


class Component(object):
    """
    A component creates an option group that all live in the same config
    namespace and get accessed together.

    :param config_manager: Config manager pool to read options from.
    :type config_manager: ConfigManager
    :param namespace: Namespace that the compnent should be searched in.
    :type namespace: list(str), optional
    """

    def __init__(self, config_manager, namespace=None):
        self._config_manager = config_manager
        self._namespace = namespace

    def get(self, name, default=NO_VALUE):
        """Get a raw value from the config manager pool.

        Managing parsers, validations etc are all part of the Option and so
        calling get() directly will not invoke that logic. It is therefore
        recommended that users use the option accessor which will call this
        function.

        :param name: The name of the option to fetch.
        :type name: str
        :param default: A default value to return if not found.
        """
        value = self._config_manager.get(name, namespace=self._namespace)

        if value is NO_VALUE:
            return default

        return value
