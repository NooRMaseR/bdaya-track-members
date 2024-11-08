from import_export import resources
from django.core.exceptions import PermissionDenied
from .models import GraphicDesginMember, PythonMember, CCharpMember

class MainRecource(resources.ModelResource):
    allowed_group: str
    
    def get_import_id_fields(self):
        return ['user_code']
    
    def before_import(self, dataset, **kwargs):
        user = kwargs.get('user')
        if not user:
            raise PermissionDenied("User not found.")
        
        # This should be customized in each child class based on allowed group
        if not self.is_user_allowed(user):
            raise PermissionDenied("You do not have permission to import data for this resource.")
    
    def is_user_allowed(self, user):
        return user.is_superuser or user.groups.filter(name=self.allowed_group).exists()
    
    class Meta:
        import_id_fields = ['user_code']

class PythonMemberResource(MainRecource):
    allowed_group = 'Python Admin'
    
    class Meta:
        model = PythonMember

class CCharpMemberResource(MainRecource):
    allowed_group = "C # Admin"
    
    class Meta:
        model = CCharpMember

class GraphicDesginMemberResource(MainRecource):
    allowed_group = "Graphic Desgin Admin"
    class Meta:
        model = GraphicDesginMember
    
