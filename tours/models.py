from django.db import models
from django.utils.text import slugify
from datetime import datetime
from datetime import timedelta


class Departure(models.Model):
    slug = models.SlugField(max_length=100, blank=True)
    title = models.CharField(max_length=100)
        
    class Meta:
        verbose_name = 'Места назначения (для туров)'
        verbose_name_plural = 'Места назначения (для туров)'

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Departure, self).save(*args, **kwargs)