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
    list_display = ['name','user_admin','name_area','image_store']
    #list_display_links = ['user_admin']
    list_editable = ['user_admin','image_store','name_area']
    search_fields = ['name','address_store','name_area']
    list_filter = ['user_admin','city','name_area']
admin.site.register(Store,StoreAdmin)


## Profile
class ProfileImportExport(ImportExportModelAdmin):
    pass

admin.site.register(Profile,ProfileImportExport)



class ItemAdmin(admin.ModelAdmin):
    list_display = ['name','type_parent','image']

    list_editable = ['type_parent','image']
    list_filter = ['type_parent']


admin.site.register(Item,ItemAdmin)

admin.site.register(Tags)
class VisitAdmin(admin.ModelAdmin):
    list_display = ['store','type_of','short_desc',
    'done','argent','date_visit',
    'send_by','fixed_by','describe_proplem'
    ]
    #list_display_links = ['user_admin']
    list_editable = ['type_of','short_desc',
    'done','argent','date_visit',
    'send_by','fixed_by',
        ]
    search_fields = ['store','short_desc','faults','describe_proplem']
    list_filter = ['store','type_of','send_by']

class FaultAdmin(admin.ModelAdmin):
    list_display = ['name','item','status',
    'quantity','visit','created_by',
    'created_at','belong_to','active'
    ]
    #list_display_links = ['user_admin']
    list_editable = ['item','status','created_by',
    'quantity','visit','belong_to','active'
        ]
    search_fields = ['visit','name','item']
    list_filter = ['belong_to','created_by','item','fixed_at']


admin.site.register(Visit,VisitAdmin)

admin.site.register(Fault,FaultAdmin)
admin.site.register(ImageFault)