# Generated by Django 2.2.24 on 2021-09-08 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consignment', '0029_auto_20210908_1054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderconsignment',
            name='num',
        ),
    ]
