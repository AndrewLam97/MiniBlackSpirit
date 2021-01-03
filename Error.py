class Error(Exception):
    """
    Base class for other exceptions
    """
    pass

class LengthError(Error):
    """
    Raised when two lists are of different lengths
    """
    pass