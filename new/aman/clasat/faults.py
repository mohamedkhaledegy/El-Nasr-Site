from django.db import models
from django.contrib.auth import login ,logout , authenticate
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.text import slugify

from aman import *


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
    fixed_at = models.DateTimeField(verbose_name='وقت اصلاح المشكلة',blank=True, null=True)
    belong_to = models.ForeignKey('aman.Store',on_delete=models.PROTECT,blank=True,null=True)

    def __str__(self):
        return self.name

    def get_visits(self):
        pass