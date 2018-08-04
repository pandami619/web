from django.db import models


class Novelties(models.Model):
    title = models.CharField(max_length=10, verbose_name='Имя продукта')
    text = models.CharField(max_length=32, verbose_name='Краткий текст')
    image = models.ImageField(upload_to='image', blank=True, null=True, verbose_name='Фото')
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Цена',
                                default='0')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Новинка"
        verbose_name_plural = "Новинки"


class Logo(models.Model):
    title = models.CharField(max_length=15)
    text = models.TextField()

    def __str__(self):
        return self.title
