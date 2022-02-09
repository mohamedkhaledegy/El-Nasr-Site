# Generated by Django 4.0.2 on 2022-02-09 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aman', '0010_alter_item_visit_fault'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='faults',
            field=models.ManyToManyField(blank=True, to='aman.Fault', verbose_name='اصلاح بواسطة'),
        ),
        migrations.AlterField(
            model_name='fault',
            name='item',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='aman.item'),
        ),
        migrations.CreateModel(
            name='ImageFault',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Faults/')),
                ('fault', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aman.visit', verbose_name='الزيارة')),
            ],
        ),
    ]
