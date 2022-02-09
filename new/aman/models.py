
from distutils.command.upload import upload
from logging import PlaceHolder
from operator import mod
from pydoc import describe
from re import T
from tkinter import N
from django.db import models
from django.contrib.auth import login ,logout , authenticate
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.text import slugify

import aman

app_name = 'aman'

# Create your models here.

class Profile(models.Model):
    pos_site = (
        ('Admin','Admin' ),
        ('Manager','Manager'),
        ('Quality','Quality'),
        ('Technical','Technical'),
        ('Sales','Sales'),
        ('ElNasr','ElNasr'),
        ('default','default'),
    )
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50 ,verbose_name="الاسم الاول", blank=True, null=True)
    last_name = models.CharField(max_length=50 ,verbose_name="اللقب", blank=True, null=True)
    phone_number = models.CharField(max_length=11,verbose_name="رقم التليفون",null=True , blank=True)
    phone_number2 = models.CharField(max_length=11,verbose_name="رقم التليفون 2",null=True , blank=True)
    addres = models.CharField(max_length=300 ,verbose_name="العنوان", blank=True, null=True)
    area = models.CharField(max_length=50 ,verbose_name="المنقطة", blank=True, null=True)
    mailo = models.EmailField(max_length=254,verbose_name="ايميل (بالشركة)", blank=True, null=True)
    image = models.ImageField(upload_to="Profiles/",verbose_name="صورة شخصية",blank=True, null=True)
    stores = models.ManyToManyField('aman.Store',verbose_name="الفروع المسئول عنها",blank=True)    
    title = models.CharField(max_length=50 ,verbose_name="المسمى الوظيفى", blank=True, null=True)
    pos_in_store = models.CharField(max_length=50 ,choices=pos_site,verbose_name="صفته بالموقع", blank=True, null=True)

    def __str__(self):
        return str(self.user)

@receiver(post_save , sender=User)
def create_user_profile(sender,instance,created , **kwargs):
    if created:
        Profile.objects.create(
            user = instance
        )
class Tags(models.Model):
    name_tag = models.CharField(max_length=50,unique=True)
    def __str__(self):
        return self.name_tag

class AdmenAman(models.Model):
    name = models.CharField(verbose_name=("الاسم"), max_length=50)
    mobile_num = models.CharField(max_length=11,  verbose_name='رقم الموبايل')
    mobile_num2 = models.CharField(verbose_name=("رقم الموبايل 2"), max_length=11, blank=True,null=True)
    email_address = models.EmailField(verbose_name=("الايميل"), blank=True,null=True)
    tag = models.ManyToManyField(Tags,verbose_name=("Tag"), blank=True)
    name_area = models.CharField(verbose_name=("اسم المنطقة"), max_length=20, blank=True, null=True)
    slug = models.SlugField(blank=True,null=True)
    def save(self , *args , **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(AdmenAman,self).save(*args, **kwargs)
    def __str__(self):
        return self.name

class Store(models.Model):
    name = models.CharField( max_length=200,verbose_name=("اسم الفرع"),unique=True)
    image_store = models.ImageField(upload_to="Stores/MainPic",blank=True,null=True,verbose_name='صورة الفرع')
    monthly_visited = models.BooleanField(default=True, verbose_name='زيارة شهرية',blank=True,null=True)
    user_admin_all = models.ForeignKey(User , blank=True,null=True,on_delete=models.PROTECT,related_name='user_admin_full',verbose_name="ادمين الفرع")
    user_admin = models.ForeignKey(User , blank=True,null=True,on_delete=models.PROTECT,to_field='username',related_name='user_admin',verbose_name="ادمين الفرع")
    user_staff = models.ForeignKey(User, blank=True,null=True,on_delete=models.PROTECT,to_field='username',related_name='user_staff',verbose_name="موظف الفرع")
    admen = models.ForeignKey("aman.AdmenAman", verbose_name=("ادمين الفرع حاليا"), on_delete=models.DO_NOTHING , blank=True,null=True)
    active = models.BooleanField(default=True, verbose_name='يعمل',blank=True,null=True)
    name_area = models.CharField(verbose_name=("اسم المنطقة"), max_length=20, blank=True, null=True)
    line = models.CharField(verbose_name=("خط السير"), max_length=50 ,blank=True, null=True)
    city = models.CharField(verbose_name=("المدينة"), max_length=50,blank=True, null=True)
    address_store = models.CharField(verbose_name=("العنوان"), max_length=1000,blank=True,null=True)
    location_store = models.CharField(max_length=1000, verbose_name="الموقع",blank=True,null=True)
    tag = models.ManyToManyField(Tags,verbose_name=("Tag"), blank=True)
    slug = models.SlugField(blank=True, null=True)
    
    def save(self , *args , **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Store,self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return str(self.name)

class FixRequest(models.Model):
    emergency_type = (
        ("Urgent","Urgent"),
        ("Important","Important"),
        ("Postpone","Postpone")
       )
    short_desc = models.CharField(max_length=200 ,verbose_name='وصف قصير للمشكلة')
    store = models.ForeignKey(Store ,verbose_name='الفرع',null=True, blank=True, on_delete=models.SET_NULL)
    admen_aman = models.ForeignKey(AdmenAman, verbose_name='الادمن المسئول' , on_delete=models.SET_NULL,null=True,blank=True)
    date_created = models.DateTimeField(auto_now=True,verbose_name='تايخ الطلب')
    date_modified = models.DateTimeField(auto_now_add=True,verbose_name='اخر تعديل')
    monthly_visited = models.BooleanField(default=True, verbose_name='مع الزيارة الشهرية')
    emergency = models.CharField(max_length=100,blank=True, null=True,verbose_name='درجة الأهمية',choices=emergency_type)
    slug = models.SlugField(blank=True, null=True)

    def save(self , *args , **kwargs):
        if not self.slug:
            self.slug = slugify(self.short_desc)
        super(FixRequest,self).save(*args, **kwargs)

    def __str__(self):
        return self.short_desc[:15]

class Item(models.Model):
    item_types = (
        ('دهانات','دهانات'),
        ('قطع غيار','قطع غيار'),
        ('تركيبات','تركيبات'),
        ('كهرباء','كهرباء'),
        ('زجاج','زجاج'),
        ('اكسسوارات السيكوريت','اكسسوارات السيكوريت'),
        ('تكييف','تكييف'),
        ('نقل','نقل'),
        ('معاينة','معاينة'),
        ('رفع مقاسات','رفع مقاسات'),
        ('ستاندات','ستاندات'),
        ('علب خشبية','علب خشبية'),
        ('جيبسون بورد','جيبسون بورد'),
        ('كلادينج','كلادينج'),
        ('الباب الصاج','الباب الصاج'),
        ('ستانلس','ستانلس'),
    )
    name = models.CharField(verbose_name=("اسم القطعة-الخدمة"), max_length=100)
    describe_item = models.TextField(verbose_name=("وصف القطعة"),blank=True, null=True)
    type_parent = models.CharField(verbose_name=("النوع"),max_length=100,choices=item_types)
    image = models.ImageField(upload_to='Items/',blank=True,null=True,verbose_name='صورة القطعة')
    status = models.BooleanField(default=False , verbose_name="حالة العطل")
    visit = models.ForeignKey('aman.Visit',on_delete=models.PROTECT,blank=True,null=True)

    def __str__(self):
        return str(self.name)

class ImageFault(models.Model):
    fault = models.ForeignKey('aman.Visit',on_delete=models.SET_NULL, blank=True, null=True,verbose_name="الزيارة")
    image = models.ImageField(upload_to='Faults/')

class Fault(models.Model):
    name = models.CharField(verbose_name=("اسم العطل"), max_length=100)
    item = models.OneToOneField('aman.Item',on_delete=models.PROTECT,blank=True,null=True)
    status = models.BooleanField()
    quantity = models.PositiveIntegerField()
    visit = models.ForeignKey('aman.Visit', related_name='fault_visit',on_delete=models.PROTECT,blank=True,null=True,verbose_name='الزيارة')

    def __str__(self):
        return self.name

class Visit(models.Model):
    types_visit = (
        ('شهرية','شهرية') ,
        ('طارئة','طارئة') ,
        ('شهرية-تكميلية','شهرية-تكميلية') ,
        ('معاينة','معاينة') ,
        )
    store = models.ForeignKey(Store ,verbose_name='الفرع',null=True, blank=True, on_delete=models.PROTECT)
    
    type_of = models.CharField(max_length=100,blank=True, null=True,verbose_name='نوع الزيارة',choices=types_visit)
    short_desc = models.CharField(max_length=300,blank=True, null=True,verbose_name=('ملخص المشكلة'))
    describe_proplem = models.TextField(max_length=3000,blank=True, null=True,verbose_name=('وصف المشكلة'))
    done = models.BooleanField(default=False)
    argent = models.BooleanField(default=False)
    created_by = models.ForeignKey("aman.AdmenAman", verbose_name='انشاء بواسطة',on_delete=models.PROTECT,blank=True, null=True)
    date_created = models.DateTimeField(auto_now=True,verbose_name='وقت تقديم الطلب')
    date_visit = models.DateTimeField(verbose_name='موعد الزيارة',blank=True,null=True)
    content = models.ManyToManyField("aman.Item",related_name='items', verbose_name=("الوحدة"),blank=True)
    fixed_by = models.ForeignKey('aman.Profile',on_delete=models.PROTECT,blank=True, null=True,verbose_name="اصلاح بواسطة")
    send_by = models.ForeignKey('aman.Profile',on_delete=models.PROTECT, related_name='sendby' ,blank=True, null=True,verbose_name="ارسال بواسطة")
    faults = models.ManyToManyField('aman.Fault',related_name='visit_faults',blank=True,verbose_name="اصلاح بواسطة")

    def save(self , *args , **kwargs):
        if not self.short_desc:
            self.short_desc = 'زيارة ' + str(self.type_of) + ' لفرع : ' + str(self.store)
        super(Visit,self).save(*args, **kwargs)
    def __str__(self):
        return str(self.short_desc)



class ImageVisit(models.Model):
    store = models.ForeignKey('aman.Store',on_delete=models.SET_NULL, blank=True, null=True,verbose_name="الفرع")
    visit = models.ForeignKey('aman.Visit',on_delete=models.SET_NULL, blank=True, null=True,verbose_name="الزيارة")
    image = models.ImageField(upload_to='Visits/')