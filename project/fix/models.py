from django.db import models
from django.db.models.enums import Choices
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.

class Fix(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True )
    slug = models.SlugField(blank=True, null=True)


    def __str__(self):
        return 

    def save(self , *args , **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Fix,self).save(*args, **kwargs)