from django.db import models


class ProductCategory(models.Model):
    title = models.CharField(max_length=64, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категория товаров'


class Production(models.Model):
    title = models.CharField(max_length=32, blank=True, null=True, default=None, verbose_name='Имя гриля')
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Цена', default=0)
    discount = models.IntegerField(default=0, verbose_name='Скидка')
    category = models.ForeignKey(ProductCategory, blank=True, null=True, default=None, on_delete=models.DO_NOTHING)
    short_description = models.TextField(blank=True, null=True, default=None, verbose_name='Короткое описание')
    description = models.TextField(blank=True, null=True, default=None, verbose_name='Описание')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f"{self.price} {self.title}"
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductionImage(models.Model):
    product = models.ForeignKey(Production, blank=True, null=True, default=None, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to='image')
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
