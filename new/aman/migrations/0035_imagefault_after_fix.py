# Generated by Django 4.0.2 on 2022-02-18 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aman', '0034_alter_item_type_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagefault',
            name='after_fix',
            field=models.BooleanField(default=False),
        ),
    ]
