
from datetime import date, datetime
from django.db import models
from django.contrib.auth import login ,logout , authenticate
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.text import slugify

from aman import *

class Visit(models.Model):
    types_visit = (
        ('شهرية','شهرية') ,
        ('طارئة','طارئة') ,
        ('شهرية-تكميلية','شهرية-تكميلية') ,
        ('معاينة','معاينة') ,
        )
    store = models.ForeignKey('aman.Store' ,verbose_name='الفرع',null=True, blank=True, on_delete=models.PROTECT)
    type_of = models.CharField(max_length=100,blank=True, null=True,verbose_name='نوع الزيارة',choices=types_visit)
    short_desc = models.CharField(max_length=300,blank=True, null=True,verbose_name=('ملخص المشكلة'))
    describe_proplem = models.TextField(max_length=3000,blank=True, null=True,verbose_name=('وصف المشكلة'))
    done = models.BooleanField(default=False,verbose_name='انتهاء الزيارة')
    argent = models.BooleanField(default=False,verbose_name='طارئ')
    date_created = models.DateTimeField(auto_now=True,verbose_name='وقت تقديم الطلب')
    date_visit = models.DateTimeField(verbose_name='موعد الزيارة',blank=True,null=True)
    fixed_by = models.ForeignKey('aman.Profile',on_delete=models.SET_NULL,blank=True, null=True,verbose_name="اصلاح بواسطة")
    send_by = models.ForeignKey('aman.Profile',on_delete=models.SET_NULL, related_name='sendby' ,blank=True, null=True,verbose_name="ارسال بواسطة")
    faults = models.ManyToManyField('aman.Fault',blank=True,related_name='proplems' ,verbose_name="الأعطال")
    active = models.BooleanField(default=True)

    def save(self , *args , **kwargs):
        if not self.short_desc:
            self.short_desc = 'زيارة ' + str(self.type_of) + ' لفرع : ' + str(self.store)
        super(Visit,self).save(*args, **kwargs)
    
    def __str__(self):
        return "زيارة  - %s -  %s - شهر %s" % (self.type_of, self.store ,self.date_visit.month)

    # def get_visits_this_month(self,a):
    #     return "%s" self. = [x for x in Visit.objects.filter(date_visit__month=datetime.now.month)]
    
    