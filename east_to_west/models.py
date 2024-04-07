from django.db import models


class Contact(models.Model):
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    location = models.CharField(max_length=150)
    working_days = models.CharField(max_length=20)
    working_hours = models.CharField(max_length=20)
    google_map_url = models.TextField()

    class Meta:
        verbose_name = 'Контактная информация'
        verbose_name_plural = 'Контактная информация'

    def __str__(self):
        return 'Контактная информация'


class OurGallery(models.Model):
    image = models.ImageField(upload_to='gallery/')

    class Meta:
        verbose_name = 'Наши фото'
        verbose_name_plural = 'Наши фото'

    def __str__(self):
        return 'Фото'


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/')

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галерея'

    def __str__(self):
        return 'Фото галереи'
    

class Review(models.Model):
    text = models.TextField()
    user_name = models.CharField(max_length=100)
    user_photo = models.ImageField(upload_to='users/')
    stars = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Отзывы'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f'Отзыв от {self.user_name}'
    

class Destination(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to='tours/')
    
    class Meta:
        verbose_name = 'Места назначения'
        verbose_name_plural = 'Места назначения'

    def __str__(self):
        return self.title