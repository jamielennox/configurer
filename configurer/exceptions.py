class ConfigurerError(Exception):
    """
    Base Exception class for all Exceptions defined in configurer.
    """


class ValidationError(ConfigurerError):
    """
    An exception that is raised when a option vallue fails validation.
    """
