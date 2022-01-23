from django.shortcuts import render
from django.template import context

# Create your views here.


def index(request):
    context = {'name':'Mohamed'}
    return render(request,'index.html',context)