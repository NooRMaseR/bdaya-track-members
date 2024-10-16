from import_export import resources
from .models import PythonMember, CCharpMember

class MainRecource(resources.ModelResource):
    def get_import_id_fields(self):
        return ['user_code']
    
    class Meta:
        import_id_fields = ['user_code']

class PythonMemberResource(MainRecource):
    
    class Meta:
        model = PythonMember

class CCharpMemberResource(MainRecource):
    
    class Meta:
        model = CCharpMember
    
