# Generated by Django 2.2.24 on 2021-09-06 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0002_calculate_convert_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(db_index=True, max_length=100),
        ),
    ]
