from django.core.exceptions import ValidationError
from enum import Enum

class CODES(Enum):
    PYTHON = 'p'
    GraphicDesgin = 'd'
    CSHARP = 'c'
    CCNA = 'n'
    FRONTEND = 'f'


def validate_user_code(code: str, track_code: CODES) -> None:
    """
    Validate the Student Code
    
    the code must start with any of the valid codes

    Args:
        code (str): the student code (the numbers part)
        track_code (CODES): the track to validate

    Raises:
        ValidationError: if the first litter is not exists
        ValidationError: if `-` is not exists after the first litter
        ValidationError: if the rest of code are not numbers
    """
    
    litter, dash, rest_code = (code[0], code[1], code[2:])
    
    if litter.lower() != CODES.PYTHON.value:
        raise ValidationError(f"The First Litter Must Be Valid Code for this track which is \"{track_code.value}\"")
    
    if dash != "-":
        raise ValidationError(f"there must be a \"-\" after {track_code.value} like this \"{track_code.value}-\"")
    
    if not rest_code.isnumeric():
        raise ValidationError("This is Not A Valid Code")

def validate_py_code(full_code: str) -> None:
    """Validate a Python Student Code\n
    the code must start with any of the valid codes

    Args:
        full_code (str): the student code

    Raises:
        ValidationError: if the first litter is not exists
        ValidationError: if `-` is not exists after the first litter
        ValidationError: if the rest of code are not numbers
    """
    validate_user_code(full_code, CODES.PYTHON)

def validate_csharp_code(full_code: str) -> None:
    """Validate a C# Student Code\n
    the code must start with any of the valid codes

    Args:
        full_code (str): the student code

    Raises:
        ValidationError: if the first litter is not exists
        ValidationError: if `-` is not exists after the first litter
        ValidationError: if the rest of code are not numbers
    """
    validate_user_code(full_code, CODES.CSHARP)

def validate_graphic_desgin_code(full_code: str) -> None:
    """Validate a Graphic Desgin Student Code\n
    the code must start with any of the valid codes

    Args:
        full_code (str): the student code

    Raises:
        ValidationError: if the first litter is not exists
        ValidationError: if `-` is not exists after the first litter
        ValidationError: if the rest of code are not numbers
    """
    validate_user_code(full_code, CODES.GraphicDesgin)
    
