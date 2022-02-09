import site
from django.contrib import admin
from django.contrib.auth.models import User

from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.

admin.site.site_header = "النصر"
admin.site.site_title = "النصر"

## Store
class StoreImportExport(ImportExportModelAdmin):
    pass
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name','user_admin_all','name_area','image_store']
    #list_display_links = ['user_admin']
    list_editable = ['user_admin_all','image_store','name_area']
    search_fields = ['name','address_store','name_area']
    list_filter = ['user_admin','city','name_area']
admin.site.register(Store,StoreImportExport)


## Profile
class ProfileImportExport(ImportExportModelAdmin):
    pass

admin.site.register(Profile,ProfileImportExport)
class ItemImportExport(ImportExportModelAdmin):
    pass

admin.site.register(Item,ItemImportExport)

admin.site.register(Tags)

@admin.register(Visit)
class VisitImportExport(ImportExportModelAdmin):
    pass

admin.site.register(Fault)
admin.site.register(ImageFault)