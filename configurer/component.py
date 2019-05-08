from configurer.consts import NO_VALUE


class Component(object):

    def __init__(self, config_manager, namespace=None):
        self._config_manager = config_manager
        self._namespace = namespace

    # def __getitem__(self, name):
    #     value = self.get(name, default=NO_VALUE)
    #     if value is NO_VALUE:
    #         raise KeyError(name)
    #     return value

    def get(self, name, default=NO_VALUE):
        value = self._config_manager.get(name, namespace=self._namespace)

        if value is NO_VALUE:
            return default

        return value
