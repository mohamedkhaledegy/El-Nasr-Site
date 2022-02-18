# Generated by Django 4.0.2 on 2022-02-17 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aman', '0032_remove_storeunit_store_orderstoreunit_to_store_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='type_parent',
            field=models.CharField(blank=True, choices=[('دهانات', 'دهانات'), ('قطع غيار', 'قطع غيار'), ('تركيبات', 'تركيبات'), ('كهرباء', 'كهرباء'), ('زجاج', 'زجاج'), ('اكسسوارات السيكوريت', 'اكسسوارات السيكوريت'), ('تكييف', 'تكييف'), ('ستاندات', 'ستاندات'), ('علب خشبية', 'علب خشبية'), ('جيبسون بورد', 'جيبسون بورد'), ('كلادينج', 'كلادينج'), ('الباب الصاج', 'الباب الصاج'), ('ستانلس', 'ستانلس'), ('سيراميك ورخام', 'سيراميك ورخام'), ('اكليرك', 'اكليرك'), ('خشب', 'خشب'), ('معدن', 'معدن')], max_length=100, null=True, verbose_name='النوع'),
        ),
    ]
