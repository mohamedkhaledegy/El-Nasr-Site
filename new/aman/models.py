from tkinter import N
from venv import create
from django.db import models
from django.contrib.auth import login ,logout , authenticate
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.text import slugify

## import Models from clasat 
####
from aman.clasat.visits import *
from aman.clasat.faults import *
####
app_name = 'aman'
## Create your models here.
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
    def full_name(self):
        return "%s %s" % (self.user.profile.first_name, self.user.profile.last_name)

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

class Store(models.Model):
    name = models.CharField( max_length=200,verbose_name=("اسم الفرع"),unique=True)
    image_store = models.ImageField(upload_to="Stores/MainPic",blank=True,null=True,verbose_name='صورة الفرع')
    monthly_visited = models.BooleanField(default=True, verbose_name='زيارة شهرية',blank=True,null=True)
    user_admin = models.ForeignKey(User , blank=True,null=True,on_delete=models.PROTECT,related_name='store_admin',verbose_name="ادمين الفرع")
    user_staff = models.ForeignKey(User, blank=True,null=True,on_delete=models.PROTECT,related_name='store_staff',verbose_name="موظف الفرع")
    user_manager_store = models.ForeignKey(User, blank=True,null=True,on_delete=models.PROTECT,related_name='store_manager',verbose_name="مدير الفرع")
    active = models.BooleanField(default=True, verbose_name='يعمل',blank=True,null=True)
    name_area = models.CharField(verbose_name=("اسم المنطقة"), max_length=20, blank=True, null=True)
    line = models.CharField(verbose_name=("خط السير"), max_length=50 ,blank=True, null=True)
    city = models.CharField(verbose_name=("المدينة"), max_length=50,blank=True, null=True)
    address_store = models.CharField(verbose_name=("العنوان"), max_length=1000,blank=True,null=True)
    location_store = models.CharField(max_length=1000, verbose_name="الموقع",blank=True,null=True)
    tag = models.ManyToManyField('aman.Tags',verbose_name=("Tag"), blank=True)
    slug = models.SlugField(blank=True, null=True)
    visits = models.ManyToManyField('aman.Visit',blank=True,related_name='visitat',verbose_name='الزيارات')
    def save(self , *args , **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Store,self).save(*args, **kwargs)

    def get_visit_store(self):
        self.visits = Visit.objects.filter(store=self)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return str(self.name)
class Item(models.Model):
    item_types = (
        ('دهانات','دهانات'),
        ('قطع غيار','قطع غيار'),
        ('تركيبات','تركيبات'),
        ('كهرباء','كهرباء'),
        ('زجاج','زجاج'),
        ('اكسسوارات السيكوريت','اكسسوارات السيكوريت'),
        ('تكييف','تكييف'),
        ('ستاندات','ستاندات'),
        ('علب خشبية','علب خشبية'),
        ('جيبسون بورد','جيبسون بورد'),
        ('كلادينج','كلادينج'),
        ('الباب الصاج','الباب الصاج'),
        ('ستانلس','ستانلس'),
        ('سيراميك ورخام','سيراميك ورخام'),
        ('اكليرك','اكليرك'),
        ('خشب','خشب'),
        ('معدن','معدن'),
        ('اكسسوارات اثاث', 'اكسسوارات اثاث'),
    )
    name = models.CharField(verbose_name=("اسم القطعة-الخدمة"), max_length=100)
    describe_item = models.TextField(verbose_name=("وصف القطعة"),max_length=4000 ,blank=True, null=True)
    type_parent = models.CharField(verbose_name=("النوع"),max_length=100,choices=item_types , blank=True, null=True)
    image = models.ImageField(upload_to='Items/',blank=True,null=True,verbose_name='صورة القطعة')
    def __str__(self):
        return str(self.name)



class StoreUnit(models.Model):
    name = models.CharField(max_length=200,blank=True, null=True)
    image = models.ImageField(upload_to='StoreUnits/',blank=True,null=True,verbose_name='صورة الوحدة')
    parts = models.ManyToManyField('aman.Item',blank=True,verbose_name='قطع غيار بالوحدة')
    category = models.CharField(max_length=150,blank=True, null=True)

    def __str__(self):
        return self.name

class OrderStoreUnit(models.Model):

    store_unit = models.ForeignKey('aman.StoreUnit',on_delete=models.SET_NULL,blank=True,null=True)
    #unit = models.OneToOneField('aman.StoreUnit' ,verbose_name='الوحدة',null=True, blank=True, on_delete=models.PROTECT)
    date_created = models.DateField(auto_now=True)
    date_fixed = models.DateField(verbose_name='تاريخ التنفيذ',blank=True, null=True)
    created_by = models.ForeignKey('aman.Profile',on_delete=models.SET_NULL,blank=True, null=True)
    type_order = models.CharField(verbose_name='نوع الطلب',null=True, blank=True,max_length=150)
    from_place = models.ForeignKey('aman.Store' , related_name='from_store',verbose_name=' الفرع المنقول منه',null=True, blank=True, on_delete=models.SET_NULL)
    to_store = models.ForeignKey('aman.Store' ,verbose_name='الفرع',null=True, blank=True, on_delete=models.SET_NULL)
    fault = models.OneToOneField('aman.Fault',on_delete=models.PROTECT,blank=True, null=True)

    def __str__(self):
        return str(self.store_unit)
    
    
@receiver(post_save , sender=OrderStoreUnit)
def create_fault_like_order(sender,instance,created , **kwargs):
    if created:
        Fault.objects.create(
            name =  str(instance.type_order) + ' ' + str(instance.store_unit),
            status=True,
            belong_to=instance.to_store,
            created_by = instance.created_by,
        )