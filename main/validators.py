from django.core.exceptions import ValidationError
from enum import Enum

class CODES(Enum):
    PYTHON = 'p'
    GraphicDesgin = 'd'
    CSHARP = 'c'
    CCNA = 'n'
    FRONTEND = 'f'


def validate_user_code(code: str) -> None:
    """Validate the Student Code\n
    the code must start with any of the valid codes

    Args:
        code (str): the student code (the numbers part)

    Raises:
        ValidationError: if the rest of code are not numbers
    """
    
    if not code.isnumeric():
        raise ValidationError("This is Not A Valid Code")

def validate_py_code(full_code: str) -> None:
    """Validate a Python Student Code\n
    the code must start with any of the valid codes

    Args:
        full_code (str): the student code
        requeired_code (str): the track code to check

    Raises:
        ValidationError: if the first litter is not exists
        ValidationError: if the rest of code are not numbers
    """
    litter ,code = full_code[0], full_code[2:]
    
    if not litter.lower() == CODES.PYTHON.value:
        raise ValidationError(f"The First Litter Must Be Valid Code for this track which is \"{CODES.PYTHON.value}\"")
    
    validate_user_code(code)

def validate_csharp_code(full_code: str) -> None:
    """Validate a C# Student Code\n
    the code must start with any of the valid codes

    Args:
        full_code (str): the student code
        requeired_code (str): the track code to check

    Raises:
        ValidationError: if the first litter is not exists
        ValidationError: if the rest of code are not numbers
    """
    litter ,code = full_code[0], full_code[2:]
    
    if not litter.lower() == CODES.CSHARP.value:
        raise ValidationError(f"The First Litter Must Be Valid Code for this track which is \"{CODES.CSHARP.value}\"")
    
    validate_user_code(code)

def validate_graphic_desgin_code(full_code: str) -> None:
    """Validate a Graphic Desgin Student Code\n
    the code must start with any of the valid codes

    Args:
        full_code (str): the student code
        requeired_code (str): the track code to check

    Raises:
        ValidationError: if the first litter is not exists
        ValidationError: if the rest of code are not numbers
    """
    litter ,code = full_code[0], full_code[2:]
    
    if not litter.lower() == CODES.GraphicDesgin.value:
        raise ValidationError(f"The First Litter Must Be Valid Code for this track which is \"{CODES.GraphicDesgin.value}\"")
    
    validate_user_code(code)
    
