import logging
import os

from configurer.consts import NO_VALUE
from configurer.readers.base import ConfigReader


class EnvironmentReader(ConfigReader):

    LOG = logging.getLogger(__name__)

    def __init__(self, prefix=''):
        super(EnvironmentReader, self).__init__()
        self._prefix = prefix.upper()

    def _environment_variable_name(self, name, namespace=None):
        namespace = [n.upper() for n in namespace] if namespace else []
        prefix = [self._prefix.upper()] if self._prefix else []
        return '_'.join(prefix + namespace + [name.upper()])

    def get(self, name, namespace=None):
        n = self._environment_variable_name(name, namespace)

        try:
            value = os.environ[n]
        except KeyError:
            self.LOG.debug('Read Miss: %s', n)
            return NO_VALUE
        else:
            self.LOG.info('Read Found: %s', n)
            return value
