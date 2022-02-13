from datetime import datetime
from aman.models import *
from django.http import HttpResponseRedirect
from django.shortcuts import render ,redirect, get_object_or_404 , get_list_or_404 
from django.core.paginator import Paginator
from django.db.models import Count 
from django.db.models import Q
from aman.forms import *
from aman.filters import *

def profile(request):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile,user=request.user)
    else:
        profile = None
    
    stores = Store.objects.all()
    store_admin = Store.objects.filter(user_admin=profile.user)
    
    num_of_admin_stores = store_admin.count()
    this_month = datetime.now().month
    print(this_month)
    visit_filter = Visit.objects.filter(date_visit__month=this_month,send_by=request.user.id)
    visitat = Visit.faults
    print("visitat")
    print(visitat)
    print("Number of Visit for my Branch")
    print(visit_filter.count())
    fault_filter = Fault.objects.filter(created_at__month=this_month)
    if ['name_of_store'] in request:
        store_choosen = request['name_of_store']
    else:
        store_choosen = None
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    
    print(ip)

    print("Visit Filters count is >>")
    print(visit_filter.count())
    context = {
        #### محتويات البروفايل

        'profile':profile, ## جيع معلومات البروفايل
        'stores':stores, ## الفروع كاملة
        'stores_user':store_admin,  ## فروع الادمين
        'num_of_admin_stores':num_of_admin_stores, ## عدد فروع الادمين
        'this_month':this_month, ### الشهر الحالى
        'visits_this_month':visit_filter, ### الزيارات للشهر الحالى
        'faults_this_month':fault_filter, ### الاعطال للشهر الحالى
        'store_choosen':store_choosen,

    }
    return render(request,'profile/profile.html',context)
