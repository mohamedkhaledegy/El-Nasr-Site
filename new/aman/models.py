from django.db import models
from django.contrib.auth import login ,logout , authenticate
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.text import slugify

## Visit Model
####
from aman.clasat.visit import Visit
####

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
    tag = models.ManyToManyField(Tags,verbose_name=("Tag"), blank=True)
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
    
    def __str__(self):
        return str(self.name)

class ImageFault(models.Model):
    fault = models.ForeignKey('aman.Fault',on_delete=models.SET_NULL, blank=True, null=True,verbose_name="العطل")
    image = models.ImageField(upload_to='Faults/')

class Fault(models.Model):
    name = models.CharField(verbose_name=("اسم العطل"), max_length=100)
    describe = models.TextField(max_length=3000,blank=True, null=True,verbose_name=('وصف المشكلة'))
    item = models.ForeignKey('aman.Item',on_delete=models.PROTECT,blank=True,null=True)
    status = models.BooleanField(verbose_name='تم الاصلاح')
    quantity = models.PositiveIntegerField(default=1)
    visit = models.ForeignKey('aman.Visit', related_name='fault_visit',on_delete=models.PROTECT,blank=True,null=True,verbose_name='الزيارة')
    created_by = models.ForeignKey('aman.Profile',on_delete=models.PROTECT, related_name='created_by' ,blank=True, null=True,verbose_name="ارسال بواسطة")
    created_at = models.DateTimeField(auto_now=True,verbose_name='وقت ارسال المشكلة')
    belong_to = models.ForeignKey('aman.Store',on_delete=models.PROTECT,blank=True,null=True)

    def __str__(self):
        return self.name

    def get_visits(self):
        pass