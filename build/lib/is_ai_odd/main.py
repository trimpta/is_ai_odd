from .validation import _valid
from .api import gemini



def _is_odd(x: int, model: gemini) -> bool:

    if not _valid(x):
        raise TypeError
    
    response = model.num_response(x)

    if "yes" in response.lower():
        return True
    else:
        return False    
    