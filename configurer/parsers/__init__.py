
__all__ = [
    'boolean',
    'list',
]


def boolean(value):
    if isinstance(value, bool):
        return value


def list(parser, delimiter=','):
    def _listparser(value):
        return [parser(v) for v in value.split(delimiter)]

    return _listparser
