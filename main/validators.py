from django.core.exceptions import ValidationError

def validate_user_code(full_code: str) -> None:
    litter ,code = full_code[0], full_code[1:]
    if not (litter.isalpha() or code.isnumeric()):
        raise ValidationError("This is Not A Valid Code")