from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserAccountManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError('Поле email обязательно')       
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True
        user.is_active = True
        user.save()
        return user


class Profile(AbstractBaseUser):
    email = models.EmailField(verbose_name='Email', unique=True)
    phone = models.CharField(max_length=20, null=True, verbose_name='Номер телефона', blank=True)
    city = models.CharField(max_length=50, null=True, verbose_name='Город', blank=True)
    name = models.CharField(max_length=50, null=True, verbose_name='Имя', blank=True)
    surname = models.CharField(max_length=50, null=True, verbose_name='Фамилия', blank=True)
    is_active = models.BooleanField(default=False, null=True)
    is_admin = models.BooleanField(default=False, null=True)
    is_superuser = models.BooleanField(default=False, null=True)
    is_staff = models.BooleanField(default=False, null=True)
    USERNAME_FIELD = 'email'
    
    objects = UserAccountManager()

    def has_perms(self, perm, obj=None):
        return True

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    @property
    def present(self):
        value_to_present = self.email.strip().split('@')[0]
        return value_to_present