# Generated by Django 2.2.24 on 2021-09-08 07:52

import common.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consignment', '0027_auto_20210908_0956'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderconsignment',
            name='num',
            field=common.utils.OrderField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orderconsignment',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
