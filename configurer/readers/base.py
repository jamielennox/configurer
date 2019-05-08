class ConfigReader(object):
    """Base class for implementing a Reader."""

    def get(self, name, namespace=None):
        """Retrieve a value from a configuration source.

        :param name: The name of the value to retrieve.
        :type name: str
        :param namespace: Namespace to retrieve option from.
        :type namespace: list(str), Optional
        """
        raise NotImplementedError()
