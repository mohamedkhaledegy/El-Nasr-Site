from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index , name='home' ),
    path('stores/', views.store_list , name='stores' ),
    path('stores/<slug:slug>/', views.store_detail , name='store_details' ),
    path('faults/list', views.fault_list , name='fault_list' ),
    path('faults/<int:id_fault>', views.fault_detail , name='fault_list' ),

    path('faults/new', views.fault_new , name='fault_new' ),
    path('faults/edit', views.fault_edit , name='fault_edit' ),

    path('visit/new/', views.new_visit , name='new_visit' ),
    path('visit/list/', views.visits_list , name='visit_list' ),
    path('visit/list/mystores/', views.visit_list_admin , name='visit_list_admin' ),
    path('visit/<int:id>/', views.visit_detail , name='visit_detail' ),
    path('<slug:slug>/visit/list/', views.visit_list_store , name='visit_list_store' ),
    path('<slug:slug>/visit/new/', views.new_visit_emergency , name='new_visit_emergency' ),
    path('profile/', views.profile , name='profile' ),
    path('faults/list', views.fault_list , name='fault_list' ),
    path('faults/new', views.fault_new , name='fault_new' ),
    path('faults/edit', views.fault_edit , name='fault_edit' ),
]