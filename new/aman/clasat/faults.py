from urllib import request
from django.db import models
from django.contrib.auth import login ,logout , authenticate
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import ModelMultipleChoiceField
from django.utils import timezone
from django.utils.text import slugify
class ImageFault(models.Model):
    fault = models.ForeignKey('aman.Fault',on_delete=models.SET_NULL, blank=True, null=True,verbose_name="العطل")
    image = models.ImageField(upload_to='Faults/')
    describ = models.CharField(max_length=1000,verbose_name="وصف الصورة",blank=True, null=True)
    date = models.DateTimeField(auto_now=True)
    after_fix = models.BooleanField(default=False)
    def __str__(self):
        return str(self.fault)
class Fault(models.Model):
    class ChoicesStatus(models.TextChoices):
        FRESHMAN = 'SID', ('Send')
        SOPHOMORE = 'FIX', ('Fixed')
        JUNIOR = 'CHK', ('Checked')
        SENIOR = 'SUS', ('Suspended')
        GRADUATE = 'CNL', ('Cancelled')

    actionat = (
        ('send','send'),
        ('check','check'),
        ('repair','repair'),
        ('finish','finish'),
            )
    stats_chois = (
        ('sent','sent'),
        ('checked','checked'),
        ('fixed','Fixed'),
        ('reviewed','reviewed')
            )
    name = models.CharField(verbose_name=("ملخص المشكلة"), max_length=100)
    describe = models.TextField(max_length=3000,blank=True, null=True,verbose_name=('وصف المشكلة'))
    item = models.ForeignKey('aman.Item',on_delete=models.PROTECT,blank=True,null=True)
    status = models.BooleanField(verbose_name='تم الاصلاح')
    quantity = models.PositiveIntegerField(default=1)
    visit = models.ForeignKey('aman.Visit', related_name='fault_visit',on_delete=models.PROTECT,blank=True,null=True,verbose_name='الزيارة')
    created_by = models.ForeignKey('aman.Profile',on_delete=models.PROTECT, related_name='created_by' , blank=True, null=True,verbose_name="انشاء بواسطة")
    created_at = models.DateTimeField(auto_now=True,verbose_name='وقت ارسال المشكلة')
    fixed_at = models.DateTimeField(verbose_name='وقت اصلاح المشكلة',blank=True, null=True)
    belong_to = models.ForeignKey('aman.Store',on_delete=models.PROTECT,blank=True,null=True,verbose_name='الفرع')
    active = models.BooleanField(default=False , verbose_name='اظهار العطل')
    active_tosend = models.BooleanField(default=True , blank=True , verbose_name='ارسال العطل الى الصيانة')
    need_to_approve = models.BooleanField(default=False ,  blank=True ,verbose_name='اصلاح يحتاج الى موافقة')
    approved_to_repair = models.BooleanField(default=False , blank=True ,verbose_name='تم الموافقة على الاصلاح')
    action_to_fault = models.CharField(max_length=100 ,default='send',verbose_name='الاجراء المتخذ',choices=actionat)
    status_choice = models.CharField(max_length=120,default='sent' ,verbose_name='اختيارات الحالة',choices=stats_chois)
    choices_el_status = models.CharField(max_length=33,
        choices=ChoicesStatus.choices,
        default=ChoicesStatus.FRESHMAN,)
        
    def __str__(self):
        return self.name + " لفرع " + str(self.belong_to)

    def set_store_visit(self,*args,**kwargs):
        if not self.belong_to :
            self.belong_to = self.visit.store
            print(self.belong_to)
        super(Fault,self).save(*args,**kwargs)
