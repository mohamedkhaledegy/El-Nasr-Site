from django.urls import path 
from . import views



urlpatterns = [
    path('', views.index , name='home' ),
    ## الادارة ####### by pos in store
    path('manage/',views.manage,name='manage'),
    #### عرض للفروع والاعطال والزيارات حسب الاختصاص
    
    path('stores/', views.store_list , name='stores' ),
    #### عرض الفروع كاملة بتفاصيل عنها وتفاصيل عن الادمين  ###### مفتوح فقط ل manager-quality-elnasr
    path('stores/list/', views.store_list_details , name='stores_visits_faults' ),
    #### عرض الفروع بكل تفاصيلها من بيانات واعطال وزيارات وطلبات
    path('stores/<slug:slug>/', views.store_detail , name='store_details' ),
    #### عرض الفرع بتفاصيله وبياناته واخر زيارات ليه واعطال لسة ما اتحلتش

    path('faults/list', views.fault_list , name='fault_list' ),
    #### الاعطال كاملة 


    path('faults/<int:id_fault>', views.fault_detail , name='fault_list' ),
    path('faults/new', views.fault_new_admen , name='fault_new' ),
    path('faults/edit', views.fault_edit , name='fault_edit' ),

    path('visit/new/', views.new_visit , name='new_visit' ),
    path('visit/list/', views.visits_list , name='visit_list' ),
    path('visit/list/mystores/', views.visit_list_admin , name='visit_list_admin' ),
    path('visit/<int:id>/', views.visit_detail , name='visit_detail' ),
    path('visit/<int:visit_id>/<int:fault_id>/', views.visit_fault_edit , name='visit_fault_edit' ),
    path('units/orders',views.order_unit_list , name='order_unit_list'),

    path('<slug:slug>/visit/list/', views.visit_list_store , name='visit_list_store' ),
    path('<slug:slug>/visit/new/', views.new_visit_emergency , name='new_visit_emergency' ),
    path('profile/', views.profile , name='profile' ),
    path('units/',views.unit_list,name='unit_list'),
    path('units/<int:unit_id>',views.unit_detail,name='unit_detail'),

]