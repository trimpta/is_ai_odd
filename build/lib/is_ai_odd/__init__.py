from .api import gemini
from .main import _is_odd

_model = None


def init(API_KEY:str) -> None:
    """Initialize core components

    Args:
        API_KEY (str): Gemini API key
    """
    
    global _model
    _model = gemini(API_KEY)

def is_odd(x: int) -> bool :
    """Checks whether given input x is odd or not

    Args:
        x (int): the number to be checked

    Returns:
        bool: returns True if the number is odd, else false
    """

    return _is_odd(x, _model)