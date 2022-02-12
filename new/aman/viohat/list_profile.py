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
        visits_admin = Visit.objects.filter(send_by=profile)
    else:
        visits_admin = None
        profile = None
    
    this_month = datetime.now().month
    visit_filter = Visit.objects.filter(date_visit__month=this_month)

    print("Visit Filters count is >>")
    print(visit_filter.count())
    stores = Store.objects.all()
    store_admin = Store.objects.filter(user_admin=profile.user)
    num_of_admin_stores = store_admin.count()
    context = {
        'profile':profile,
        'stores':stores,
        'stores_user':store_admin,
        'num_of_admin_stores':num_of_admin_stores,
        'visits_admin':visits_admin,
    }
    return render(request,'profile/profile.html',context)
