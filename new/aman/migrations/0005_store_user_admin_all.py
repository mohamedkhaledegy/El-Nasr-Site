# Generated by Django 4.0.2 on 2022-02-08 23:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aman', '0004_imagevisit'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='user_admin_all',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='user_admin_full', to=settings.AUTH_USER_MODEL, verbose_name='ادمين الفرع'),
        ),
    ]
