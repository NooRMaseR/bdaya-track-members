from django.db import models

from main.validators import validate_user_code

# Create your models here.

class BaseMember(models.Model):
    class Collages(models.TextChoices):
        CIS = "Computer information systems"
        MIS = "Mangement information systems"
        ART = "Arts"
        ENG = "Engineering"
        
    user_code = models.CharField(max_length=9, primary_key=True, validators=[validate_user_code])
    username = models.CharField(max_length=100)
    collage = models.CharField(max_length=100, choices=Collages)
    points = models.PositiveIntegerField()
    
    class Meta:
        abstract = True
    
    def __str__(self) -> str:
        return f"{self.username} - {self.user_code}"

class PythonMember(BaseMember): ...

class CCharpMember(BaseMember):
    
    class Meta:
        verbose_name_plural = "C# Members"
        verbose_name = "C# Member"

