import yaml

from configurer import ConfigReader


class YamlReader(ConfigReader):

    @classmethod
    def from_string(cls, string):
        value = yaml.safe_load(string)
        return cls(value)

    @classmethod
    def from_file(cls, filename):
        pass
