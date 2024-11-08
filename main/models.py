from django.db import models

from main.validators import (
    validate_graphic_desgin_code,
    validate_csharp_code,
    validate_user_code,
    validate_py_code,
)

# Create your models here.

class BaseMember(models.Model):
        
    user_code = models.CharField(max_length=9, primary_key=True, validators=[validate_user_code])
    username = models.CharField(max_length=100)
    points = models.PositiveIntegerField(default=0)
    
    class Meta:
        abstract = True
    
    def __str__(self) -> str:
        return f"{self.username} - {self.user_code}"

class PythonMember(BaseMember): 
    user_code = models.CharField(max_length=9, primary_key=True, validators=[validate_py_code])
    

class CCharpMember(BaseMember):
    user_code = models.CharField(max_length=9, primary_key=True, validators=[validate_csharp_code])
    
    
    class Meta:
        verbose_name_plural = "C# Members"
        verbose_name = "C# Member"

class GraphicDesginMember(BaseMember):
    user_code = models.CharField(max_length=9, primary_key=True, validators=[validate_graphic_desgin_code])
    

    class Meta:
        verbose_name_plural = "Graphic Desgin Members"
        verbose_name = "Graphic Desgin Member"

