# Generated by Django 4.0.2 on 2022-02-09 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aman', '0016_remove_visit_faults'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store',
            old_name='user_admin_all',
            new_name='user_admin',
        ),
    ]
