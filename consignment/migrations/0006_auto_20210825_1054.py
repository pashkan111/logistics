# Generated by Django 2.2.24 on 2021-08-25 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consignment', '0005_auto_20210824_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderconsignment',
            name='city_from',
            field=models.CharField(max_length=255, verbose_name='Откуда'),
        ),
        migrations.AlterField(
            model_name='orderconsignment',
            name='city_to',
            field=models.CharField(max_length=255, verbose_name='Куда'),
        ),
        migrations.AlterField(
            model_name='orderconsignment',
            name='declared_value',
            field=models.DecimalField(blank=True, decimal_places=2, default='0', max_digits=10, null=True, verbose_name='Объявленная стоимость'),
        ),
    ]
