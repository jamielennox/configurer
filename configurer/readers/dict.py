import logging

from configurer.consts import NO_VALUE
from configurer.reader import ConfigReader


class DictReader(ConfigReader):

    LOG = logging.getLogger(__name__)

    def __init__(self, values):
        self._values = values

    def get(self, name, namespace=None):
        namespace = namespace or []
        values = self._values

        debug_name = '.'.join(namespace + [name])

        for n in namespace:
            try:
                values = values[n]
            except KeyError:
                self.LOG.debug('Read Miss: %s', debug_name)
                return NO_VALUE

        try:
            value = values[name]
        except KeyError:
            self.LOG.debug('Read Miss: %s', debug_name)
            return NO_VALUE
        else:
            self.LOG.info('Read Found: %s', debug_name)
            return value
