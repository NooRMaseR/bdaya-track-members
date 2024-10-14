from import_export import resources
from .models import PythonMember, CCharpMember

class PythonMemberResource(resources.ModelResource):
    def get_import_id_fields(self):
        return ['user_id']
    class Meta:
        model = PythonMember
        import_id_fields = ['user_id']

class CCharpMemberResource(resources.ModelResource):
    def get_import_id_fields(self):
        return ['user_id']
    
    class Meta:
        model = CCharpMember
        import_id_fields = ['user_id']
    
