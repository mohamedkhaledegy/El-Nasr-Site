# Generated by Django 4.0.2 on 2022-02-09 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aman', '0013_remove_fixrequest_admen_aman_remove_fixrequest_store_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fault',
            name='item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='aman.item'),
        ),
    ]
