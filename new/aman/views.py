from datetime import datetime
from aman.models import *
from django.http import HttpResponseRedirect
from django.shortcuts import render ,redirect, get_object_or_404 , get_list_or_404 
from django.core.paginator import Paginator
from django.db.models import Count
from django.db.models import Q
from aman.forms import *
from aman.filters import *

from aman.viohat.units import *
from aman.viohat.elprofile import profile
from aman.viohat.faults import * 
from aman.viohat.visits import *
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile,user=request.user)
    else:
        profile = None
    stores = Store.objects.all()
    stores_count = stores.count()
    visit_form = 'visitform'
    store_filter = StoreFilter()
    context = {
        'test':'hello',
        'stores':stores,
        'stores_count':stores_count,
        'stores_filter':store_filter,
        'visit_form':visit_form,
        }
    return render(request,'home.html',context)

def manage(request):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile,user=request.user)
    else:
        profile = None

    stores_all = Store.objects.all()
    visits_all = Visit.objects.all().order_by('-date_visit')
    faults_all = Fault.objects.all().order_by('-created_at')

    if profile.pos_in_store == 'Quality':
        stores = stores_all
        visits = visits_all
        faults = faults_all
        form = FaultFormAdmen()
    elif profile.pos_in_store == 'Manager':
        stores = stores_all
        visits = visits_all
        faults = faults_all
        form = FaultFormAdmen()
    elif profile.pos_in_store == 'ADMIN':
        stores = stores_all.filter(user_admin=request.user)
        visits = visits_all.filter(store__in=stores)
        faults = faults_all.filter(belong_to__in=stores)
        form = FaultFormAdmen()
    elif profile.pos_in_store == "ELNASR":
        stores = stores_all
        visits = visits_all
        faults = faults_all
        form = FaultFormAdmen()

    form_default = FaultFormAdmen()

    form = []


    if request.POST:

        form = FaultFormAdmen(instance=request.POST)
        if form.is_valid():

            form.save(commit=True)
            print('Saved Form')
        else :
            form = FaultFilterAdmen()
        return redirect('/manage/')

    contex = {'stores':stores_all,'faults':faults_all,
        'visits':visits_all,'visits_count':visits_all.count(),
        'stores_count':stores_all.count(),'faults_count':faults_all.count(),
        'store_form_update':form,
        #'count_items':count_items_in_visits,
        }
    return render(request,'profile/manage.html',contex)



def store_list(request):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile,user=request.user)
    else:
        profile = None
    stores = Store.objects.all()
    visit_list = Visit.objects.all()
    if request.GET:
        store_filter = StoreFilter(request.GET)
        stores = store_filter.qs
    else:
        store_filter = StoreFilter()
    all_stores = Store.objects.all()
    store_count = stores.count()
    context = {
        'stores':all_stores,
        'storess':stores,
        'count_stores':store_count,
        'stores_filter':store_filter,
        'visitsss':visit_list,
            }
    return render(request,'store_list.html',context)

def store_list_details(request):
    return render(request,'list_stores_visits_faults.html',context)

def store_detail(request , slug):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile,user=request.user)
    else:
        profile = None
    store = get_object_or_404(Store,slug=slug)
    form = VisitForm()
    print(request.user.profile.first_name)
    print(request.session)
    print(store.user_admin)
    admin = get_object_or_404(Profile,user=store.user_admin)
    print(admin.mailo)
    stores = Store.objects.all()
    if request.method == "POST":
        form = VisitForm(request.POST)
        if form.is_valid():
            form = VisitForm(request.POST)
            #print(store)
            form_instance = form.save(commit=False)
            form_instance.store = store
            form_instance.send_by = profile
            form_instance.save()
            return redirect('/visit/list/')
        else:
            form = VisitForm()
    else:
        form = VisitForm()

    
    context = {
        'store':store,
        'admin_store':admin,
        'stores':stores,
        'form_visit':form, }
    return render(request,'store_detail.html',context)

def new_visit(request):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile,user=request.user)
    else:
        profile = None
    form = VisitForm()
    stores = Store.objects.all()
    if request.method == "POST":
        form = VisitForm(request.POST)
        if form.is_valid():
            visitform = VisitForm(request.POST)
            #print(store)
            visitform.save()
            return redirect('/stores')
        else:
            form = VisitForm()
    else:
        form = VisitForm()
    context = {
        'form_visit':form,
        'stores':stores,
    }
    return render(request,'visit/visit-new.html',context)

def visit_list(request):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile,user=request.user)
        visits_admin_stores = Visit.objects.filter(send_by=profile)
    else:
        visits_admin_stores = None
        profile = None
    visits = Visit.objects.all()
    stores = Store.objects.all()
    try:
        stores_admin = stores.filter(user_admin=profile)
    except:
        stores_admin = None
        pass
    visits_count = Visit.objects.count()
    store_count = Store.objects.count()
    faults = Fault.objects.all()
    for vis in visits:
        print(vis.store)
        print(faults.filter(belong_to=vis.store))
    context = {
        'stores':stores,
        'visits':visits,
        'stores_admin':stores_admin,
        'visits_count':visits_count,
        'count_stores':store_count,
        'visits_admin_stores':visits_admin_stores,
        'faults':faults,}
    return render(request,'visit/list.html',context)

def visit_list_admin(request):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile,user=request.user)
        visits_admin_stores = Visit.objects.filter(send_by=profile)
        stores = Store.objects.filter(user_admin=request.user)
    else:
        visits_admin_stores = None
        profile = None
    faults = Fault.objects.all()
    context = {
        'stores_admin':stores,
        'visits_admin':visits_admin_stores,
        'faults':faults,
    }
    return render(request,'visit/list_admin.html',context)

def visit_list_store(request,slug):
    stores = Store.objects.all()
    store = get_object_or_404(Store,slug=slug)
    visits_store = Visit.objects.filter(store=store)
    visits_store_count = visits_store.count()
    context = {
        'store':store,
        'stores':stores,
        'visits':visits_store,
        'visits_count':visits_store_count}
    return render(request,'visit/visit-list-store.html',context)

def visit_detail(request,id):
    visit = get_object_or_404(Visit,id=id)
    faults = Fault.objects.filter(visit=visit)
    context = {
        'visit':visit,
        'faults':faults,
    }
    return render(request,'visit/visit_detail.html',context)


def visit_by_month(request,month_visi):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile,user=request.user)
    else:
        profile = None
    visit_dynmic_monthly = Visit.objects.filter(date_visit=datetime.date)
    context = {
        'profile',
        'monthly',
    }
    return render(request,'visit/monthly.html',context)
    
# def productlist(request , category_slug=None):
#     category = None
#     productlist = Product.objects.all()
#     categorylist = Category.objects.annotate(total_products=Count('product'))
#     if category_slug :
#         category = get_object_or_404(Category ,slug=category_slug)
#         productlist = productlist.filter(category=category)
#     search_query = request.GET.get('q')
#     if search_query :
#         productlist = productlist.filter(
#             Q(name__icontains = search_query) |
#             Q(description__icontains = search_query)|
#             Q(condition__icontains = search_query)|
#             Q(brand__brand_name__icontains = search_query) |
#             Q(category__category_name__icontains = search_query) 
#         )
#     paginator = Paginator(productlist, 1) # Show 25 contacts per page
#     page = request.GET.get('page')
#     productlist = paginator.get_page(page)
#     template = 'Product/product_list.html'
#     context = {'product_list' : productlist , 'category_list' : categorylist ,'category' : category }
#     return render(request , template , context)