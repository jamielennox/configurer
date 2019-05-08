import logging

import configurer
from configurer.readers.environ import EnvironmentReader
import redis

logging.basicConfig(level=logging.DEBUG)


class RedisComponent(configurer.Component):

    host = configurer.Option('host',
                             parser=str,
                             default='localhost')

    port = configurer.Option('port',
                             parser=int,
                             default=6379)

    password = configurer.Option('password',
                                 parser=str)

    def client(self):
        kwargs = {'host': self.host, 'port': self.port}

        if self.password is not configurer.NO_VALUE:
            kwargs['password'] = self.password

        return redis.Redis(**kwargs)


cm = configurer.ConfigManager([
    EnvironmentReader('TEST')
])

redis_loader = RedisComponent(cm, ['Redis'])
client = redis_loader.client()

client.set('tester', 'hello'.encode('utf-8'))
assert client.get('tester').decode('utf-8') == 'hello'


print("**** SUCCESS ****")
