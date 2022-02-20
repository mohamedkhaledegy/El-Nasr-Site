# Generated by Django 4.0.2 on 2022-02-19 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aman', '0041_alter_orderstoreunit_options_orderstoreunit_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='fault',
            name='action_to_fault',
            field=models.CharField(choices=[('send', 'send'), ('check', 'check'), ('repair', 'repair'), ('finish', 'finish')], default='send', max_length=100, verbose_name='الاجراء المتخذ'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fault',
            name='status_choice',
            field=models.CharField(choices=[('sent', 'sent'), ('checked', 'checked'), ('fixed', 'Fixed'), ('reviewed', 'reviewed')], default='sent', max_length=120, verbose_name='اختيارات الحالة'),
            preserve_default=False,
        ),
    ]
