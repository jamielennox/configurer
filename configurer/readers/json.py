import json

from configurer.readers.dict import DictReader


class StringReader(DictReader):

    def __init__(self, json_str):
        value = json.loads(json_str)
        super(StringReader, self).__init__(value)


class FileReader(StringReader):

    def __init__(self, json_file):
        with open(json_file, 'r') as stream:
            super(FileReader, self).__init__(stream)
