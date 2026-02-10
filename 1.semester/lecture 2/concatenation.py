# run as `python3 -m doctest -v concatenation.py`
import doctest
doctest.testmod()

def concatenate(a: str, b: str)->str:
    """Concatenate two strings.
    
    Examples:
        >>> concatenate("Hi", " there!")
        'Hi there!'
        >>> concatenate("Hello", " here!")
        'Hello here!'
    """
    return a + b
