from django.db import models
from django.utils.text import slugify
from datetime import datetime
from datetime import timedelta


class TourDestination(models.Model):
    slug = models.SlugField(max_length=100, blank=True)
    title = models.CharField(max_length=100)
        
    class Meta:
        verbose_name = 'Места назначения (для туров)'
        verbose_name_plural = 'Места назначения (для туров)'

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(TourDestination, self).save(*args, **kwargs)


class TourType(models.Model):
    slug = models.SlugField(max_length=100, blank=True)
    title = models.CharField(max_length=100)
        
    class Meta:
        verbose_name = 'Типы туров'
        verbose_name_plural = 'Типы туров'

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(TourType, self).save(*args, **kwargs)


class Tour(models.Model):
    slug = models.SlugField(max_length=100, blank=True)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='tours/')
    price = models.FloatField()
    destination = models.ForeignKey(TourDestination, on_delete=models.CASCADE)
    type = models.ForeignKey(TourType, on_delete=models.CASCADE)
    descriprion = models.TextField()
    departure_time = models.DateTimeField()
    return_time = models.DateTimeField()
    persons = models.PositiveIntegerField()
    days = models.PositiveIntegerField(blank=True)
        
    class Meta:
        verbose_name = 'Туры'
        verbose_name_plural = 'Туры'

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.days = (self.return_time - self.departure_time).days

        super(Tour, self).save(*args, **kwargs)