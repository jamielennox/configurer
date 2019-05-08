
__all__ = [
    'Boolean',
    'List',
    'Or',
]


def Boolean(value):
    if isinstance(value, bool):
        return value

    if isinstance(value, int):
        return value != 0

    try:
        s = str(value).strip().lower()
    except Exception:
        pass
    else:
        if s in ('true', '1', 'on', 'yes'):
            return True
        if s in ('false', '0', 'off', 'no'):
            return False

    raise ValueError('Invalid Boolean Value: %s' % s)


def Or(*parsers):
    def _or_parser(value):
        for parser in parsers:
            try:
                return parser(value)
            except ValueError:
                pass

        raise ValueError("Can't parse or parser option: %s" % value)

    return _or_parser


def List(parser, delimiter=','):
    def _list_parser(value):
        if isinstance(value, (list, tuple)):
            pass
        elif isinstance(value, str):
            value = value.split(delimiter)
        else:
            raise ValueError('Invalid List Value: %s' % value)

        return [parser(v) for v in value]

    return _list_parser
