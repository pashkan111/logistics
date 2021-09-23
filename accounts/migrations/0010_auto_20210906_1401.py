# Generated by Django 2.2.24 on 2021-09-06 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_remove_profile_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(max_length=50, null=True, verbose_name='Город'),
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=50, null=True, verbose_name='имя'),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(max_length=20, null=True, verbose_name='Номер телефона'),
        ),
        migrations.AddField(
            model_name='profile',
            name='surname',
            field=models.CharField(max_length=50, null=True, verbose_name='Фамилия'),
        ),
    ]
