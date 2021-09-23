# Generated by Django 2.2.24 on 2021-09-07 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consignment', '0025_orderconsignment_date_of_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderconsignment',
            name='cardboard_box_amount_100',
            field=models.PositiveIntegerField(default=0, verbose_name='0,3 х 0,26 х 0,38 м. Укажите количество'),
        ),
        migrations.AddField(
            model_name='orderconsignment',
            name='cardboard_box_amount_70',
            field=models.PositiveIntegerField(default=0, verbose_name='0,3 х 0,25 х 0,17 м. Укажите количество'),
        ),
        migrations.AlterField(
            model_name='orderconsignment',
            name='cardboard_box_amount',
            field=models.PositiveIntegerField(default=0, verbose_name='0,2 х 0,19 х  0,13 м. Укажите количество'),
        ),
    ]