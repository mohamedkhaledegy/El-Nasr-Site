import site
from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.

admin.site.site_header = "النصر"
admin.site.site_title = "النصر"


class StoreImportExport(ImportExportModelAdmin):
    pass
## Store
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name','user_admin_all','name_area','image_store']
    #list_display_links = ['user_admin']
    list_editable = ['user_admin_all','image_store','name_area']
    search_fields = ['name','address_store','name_area']
    list_filter = ['user_admin','city','name_area']
admin.site.register(Store,StoreAdmin)

## Profile
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user',
    'first_name',
    'last_name',
    'phone_number',
    'phone_number2','area',
    'title']
    #list_display_links = ['user_admin']
    list_editable = [
    'first_name',
    'last_name',
    'phone_number',
    'phone_number2',
    'area',
    'title']
    search_fields = ['user']
    list_filter = ['area','title','pos_in_store']
admin.site.register(Profile,ProfileAdmin)

# Fix
class FixRequestAdmin(admin.ModelAdmin):
    list_display = ('store','short_desc', 'emergency_type','admen_aman')
    ## العواميد اللى بتظهر فى الادمين داشبورد 
admin.site.register(FixRequest, FixRequestAdmin)
 
@admin.register(Item)
class ItemImportExport(ImportExportModelAdmin):
    pass
admin.site.register(AdmenAman)
admin.site.register(Tags)
admin.site.register(ImageVisit)


@admin.register(Visit)
class VisitImportExport(ImportExportModelAdmin):
    pass

admin.site.register(Fault)
admin.site.register(ImageFault)
