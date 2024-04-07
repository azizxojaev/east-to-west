from django.db import models


class Contact(models.Model):
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    location = models.CharField(max_length=150)
    working_days = models.CharField(max_length=20)
    working_hours = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Контактная информация'
        verbose_name_plural = 'Контактная информация'

    def __str__(self):
        return 'Контактная информация'