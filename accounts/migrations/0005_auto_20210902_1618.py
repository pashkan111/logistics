# Generated by Django 2.2.24 on 2021-09-02 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210902_1237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='username',
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='wewe@mail.ru', max_length=254, unique=True, verbose_name='Email'),
            preserve_default=False,
        ),
    ]
