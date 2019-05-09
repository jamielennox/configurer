import toml

from configurer.readers.dict import DictReader


class StringReader(DictReader):

    def __init__(self, toml_str):
        value = toml.loads(toml_str)
        super(StringReader, self).__init__(value)


class FileReader(StringReader):

    def __init__(self, toml_file):
        with open(toml_file, 'r') as stream:
            super(FileReader, self).__init__(stream)
