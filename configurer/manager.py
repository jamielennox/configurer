from configurer.consts import NO_VALUE


class ConfigManager(object):

    def __init__(self, readers):
        self._readers = readers

    def get(self, name, namespace=None, default=NO_VALUE):
        for reader in self._readers:
            try:
                value = reader.get(name, namespace)
            except KeyError:
                pass

            break

        else:
            return default

        return value
