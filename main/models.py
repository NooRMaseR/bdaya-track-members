from django.db import models
from django.utils.translation import gettext_lazy as _

from main.validators import (
    validate_graphic_desgin_code,
    validate_csharp_code,
    validate_py_code,
)

# Create your models here.

class BaseMember(models.Model):
    """
    A Base Model For All Bdaya Tracks
    
    make sure to override the `user_code` property
    """
        
    user_code = models.CharField(max_length=9, primary_key=True, verbose_name=_("user code"))
    username = models.CharField(max_length=100, verbose_name= _("username"))
    points = models.PositiveIntegerField(default=0, verbose_name= _("points"))
    
    class Meta:
        abstract = True
    
    def __str__(self) -> str:
        return f"{self.username} - {self.user_code}"

class PythonMember(BaseMember): 
    user_code = models.CharField(max_length=9, primary_key=True, verbose_name=_("user code"), validators=[validate_py_code])
    
    class Meta: # type: ignore
        verbose_name_plural = _("Python Members")
        verbose_name = _("Python Member")

class CCharpMember(BaseMember):
    user_code = models.CharField(max_length=9, primary_key=True, verbose_name=_("user code"), validators=[validate_csharp_code])
    
    class Meta: # type: ignore
        verbose_name_plural = _("C# Members")
        verbose_name = _("C# Member")

class GraphicDesginMember(BaseMember):
    user_code = models.CharField(max_length=9, primary_key=True, verbose_name=_("user code"), validators=[validate_graphic_desgin_code])
    
    class Meta: # type: ignore
        verbose_name_plural = _("Graphic Desgin Members")
        verbose_name = _("Graphic Desgin Member")

