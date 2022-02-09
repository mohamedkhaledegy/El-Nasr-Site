from django.urls import path 
from . import views


urlpatterns = [
    path('', views.index , name='home' ),
    path('stores/', views.store_list , name='stores' ),
    path('stores/<slug:slug>/', views.store_detail , name='store_details' ),
    path('visit/new/', views.new_visit , name='new_visit' ),
    path('visit/list/', views.visit_list , name='visit_list' ),
    path('visit/<int:id>/', views.visit_detail , name='visit_detail' ),
    path('<slug:slug>/visit/list/', views.visit_list_store , name='visit_list_store' ),
    path('profile/', views.profile , name='profile' ),
]