# Generated by Django 4.0.2 on 2022-02-09 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aman', '0007_item_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='status',
            field=models.BooleanField(default=False, verbose_name='حالة العطل'),
        ),
    ]
