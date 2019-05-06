class _NoValue(object):

    def __nonzero__(self):
        return False

    def __bool__(self):
        return False

    def __repr__(self):
        return 'NO_VALUE'


NO_VALUE = _NoValue()
