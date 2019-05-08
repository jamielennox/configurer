import logging

import configurer
from configurer.readers.environ import EnvironmentReader
from configurer import validators
import redis

logging.basicConfig(level=logging.DEBUG)


class RedisComponent(configurer.Component):

    host = configurer.Option('host',
                             parser=str,
                             validator=[
                                 validators.Required(),
                             ],
                             default='localhost')

    port = configurer.Option('port',
                             parser=int,
                             validator=[
                                 validators.Required(),
                                 validators.GreaterThan(0),
                                 validators.LowerThan(65536),
                             ],
                             default=6379)

    password = configurer.Option('password', parser=str)

    def __init__(self, *args, **kwargs):
        super(RedisComponent, self).__init__(*args, **kwargs)
        self._client = None

    @property
    def client(self):
        if not self._client:
            kwargs = {'host': self.host, 'port': self.port}

            if self.password is not configurer.NO_VALUE:
                kwargs['password'] = self.password

            self._client = redis.Redis(**kwargs)

        return self._client


cm = configurer.ConfigManager([
    EnvironmentReader('TEST')
])

redis_loader = RedisComponent(cm, ['Redis'])
redis_loader.client.set('tester', 'hello'.encode('utf-8'))
assert redis_loader.client.get('tester').decode('utf-8') == 'hello'


print("**** SUCCESS ****")
