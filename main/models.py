from django.db import models


class Novelties(models.Model):
    title = models.CharField(max_length=10)
    text = models.TextField()
    image = models.ImageField(upload_to='image', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена',
                                default='0')

    def __str__(self):
        return self.title


class Logo(models.Model):
    title = models.CharField(max_length=15)
    text = models.TextField()

    def __str__(self):
        return self.title
