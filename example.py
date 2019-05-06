import logging

from configurer import ConfigManager, Component, Option
from configurer.readers.environ import EnvironmentReader
from configurer.validators import Required, GreaterThan, LowerThan

logging.basicConfig(level=logging.DEBUG)


cm = ConfigManager(readers=[EnvironmentReader(prefix='t')])


class DefaultConfig(Component):

    enabled = Option('enabled',
                     parser=bool,
                     default=True)

    host = Option('host',
                  parser=str,
                  validator=[
                      Required(),
                  ])

    port = Option('port',
                  parser=int,
                  validator=[
                      Required(),
                      GreaterThan(100),
                      LowerThan(1000),
                  ])

    def launch(self):
        if not self.enabled:
            return None

        return self.host, self.port


d = DefaultConfig(cm, namespace=['hello'])
print(d.launch())
