from django.db import models
from calculator.models import City


class Office(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='office_of_city', db_index=True, null=True)
    name = models.CharField(max_length=255, verbose_name='Название', null=True)
    phone = models.CharField(max_length=255, verbose_name='Телефон', null=True)
    address = models.CharField(max_length=255, verbose_name='Адрес', null=True)
    email = models.CharField(max_length=255, verbose_name='Email', null=True)
    schedule = models.CharField(max_length=255, verbose_name='Режим работы', null=True)
    coordinate1 = models.DecimalField(verbose_name='Координата1', null=True, max_digits=12, decimal_places=9)
    coordinate2 = models.DecimalField(verbose_name='Координата2', null=True, max_digits=12, decimal_places=9)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Офис'
        verbose_name_plural = 'Офисы' 