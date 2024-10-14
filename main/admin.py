from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin, GroupAdmin as BaseGroupAdmin

from unfold.contrib.import_export.forms import ExportForm, ImportForm
from main.recorces import CCharpMemberResource, PythonMemberResource
from import_export.admin import ImportExportModelAdmin
from main.models import CCharpMember, PythonMember
from unfold.admin import ModelAdmin


admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin): ...


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin): ...

# Register your models here.
@admin.register(PythonMember, CCharpMember)
class MembersModel(ModelAdmin, ImportExportModelAdmin):
    search_fields = ("user_id", "username")
    search_help_text = "Search By ID or username"
    list_filter = ("collage",)
    list_per_page = 50
    export_form_class = ExportForm
    import_form_class = ImportForm
    resource_classes = [PythonMemberResource, CCharpMemberResource]