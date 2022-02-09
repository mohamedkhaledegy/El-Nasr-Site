# Generated by Django 4.0.2 on 2022-02-09 09:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aman', '0012_fault_visit_alter_visit_faults'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fixrequest',
            name='admen_aman',
        ),
        migrations.RemoveField(
            model_name='fixrequest',
            name='store',
        ),
        migrations.RemoveField(
            model_name='imagevisit',
            name='store',
        ),
        migrations.RemoveField(
            model_name='imagevisit',
            name='visit',
        ),
        migrations.RemoveField(
            model_name='item',
            name='status',
        ),
        migrations.RemoveField(
            model_name='item',
            name='visit',
        ),
        migrations.RemoveField(
            model_name='store',
            name='admen',
        ),
        migrations.RemoveField(
            model_name='store',
            name='user_admin',
        ),
        migrations.RemoveField(
            model_name='visit',
            name='created_by',
        ),
        migrations.AddField(
            model_name='fault',
            name='describe',
            field=models.TextField(blank=True, max_length=3000, null=True, verbose_name='وصف المشكلة'),
        ),
        migrations.AddField(
            model_name='store',
            name='user_manager_store',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='store_manager', to=settings.AUTH_USER_MODEL, verbose_name='مدير الفرع'),
        ),
        migrations.AlterField(
            model_name='store',
            name='user_admin_all',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='store_admin', to=settings.AUTH_USER_MODEL, verbose_name='ادمين الفرع'),
        ),
        migrations.AlterField(
            model_name='store',
            name='user_staff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='store_staff', to=settings.AUTH_USER_MODEL, verbose_name='موظف الفرع'),
        ),
        migrations.DeleteModel(
            name='AdmenAman',
        ),
        migrations.DeleteModel(
            name='FixRequest',
        ),
        migrations.DeleteModel(
            name='ImageVisit',
        ),
    ]
