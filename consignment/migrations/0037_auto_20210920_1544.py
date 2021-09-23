# Generated by Django 2.2.24 on 2021-09-20 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consignment', '0036_auto_20210915_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderconsignment',
            name='air_bubble_amount',
            field=models.PositiveIntegerField(blank=True, default=1, null=True, verbose_name='Укажите количество'),
        ),
        migrations.AlterField(
            model_name='orderconsignment',
            name='bag_amount',
            field=models.PositiveIntegerField(blank=True, default=1, null=True, verbose_name='Укажите количество'),
        ),
        migrations.AlterField(
            model_name='orderconsignment',
            name='cardboard_box_amount',
            field=models.PositiveIntegerField(blank=True, default=1, null=True, verbose_name='0,2 х 0,19 х  0,13 м. Укажите количество'),
        ),
        migrations.AlterField(
            model_name='orderconsignment',
            name='pallet_amount',
            field=models.PositiveIntegerField(blank=True, default=1, null=True, verbose_name='Укажите количество'),
        ),
        migrations.AlterField(
            model_name='orderconsignment',
            name='pallet_board_amount',
            field=models.PositiveIntegerField(blank=True, default=1, null=True, verbose_name='Укажите количество'),
        ),
        migrations.AlterField(
            model_name='orderconsignment',
            name='rigid_packaging_amount',
            field=models.PositiveIntegerField(blank=True, default=1, null=True, verbose_name='Укажите количество'),
        ),
        migrations.AlterField(
            model_name='orderconsignment',
            name='strapping_amount',
            field=models.PositiveIntegerField(blank=True, default=1, null=True, verbose_name='Укажите количество'),
        ),
        migrations.AlterField(
            model_name='orderconsignment',
            name='stretch_amount',
            field=models.PositiveIntegerField(blank=True, default=1, null=True, verbose_name='Укажите количество'),
        ),
    ]
