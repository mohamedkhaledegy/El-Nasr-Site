from django.urls import path
from . import views

app_name = 'fix'


urlpatterns = [
    path('',views.index , name='index' ),   # الصفحة الرئيسية
]