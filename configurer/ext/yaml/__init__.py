import yaml

from configurer.readers.dict import DictReader


class StringReader(DictReader):

    def __init__(self, yaml_str):
        value = yaml.safe_load(yaml_str)
        super(StringReader, self).__init__(value)


class FileReader(StringReader):

    def __init__(self, yaml_file):
        with open(yaml_file, 'r') as stream:
            super(FileReader, self).__init__(stream)
