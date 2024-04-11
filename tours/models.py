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


class CountryHouse(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=150)
    price = models.FloatField()
    video = models.URLField()
    description = models.TextField()
    location = models.CharField(max_length=300)
    capacity = models.IntegerField()
    rooms = models.CharField(max_length=200)
    have_tv = models.BooleanField()
    have_playstation = models.BooleanField()
    have_karaoke = models.BooleanField()
    have_tenis = models.BooleanField()
    have_tapchan = models.BooleanField()
    pool = models.CharField(max_length=150)
    have_sauna = models.BooleanField()
    have_terrace = models.BooleanField()
    phone_number = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(CountryHouse, self).save(*args, **kwargs)


class HouseImage(models.Model):
    image = models.ImageField(upload_to='houses/')
    house = models.ForeignKey(CountryHouse, on_delete=models.CASCADE)