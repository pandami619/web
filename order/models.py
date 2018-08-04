from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from production.models import Production
from utils.main import disable_for_loaddata


# Create your models here.
class Status(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f"Статус {self.name}"
    
    class Meta:
        verbose_name = "Статус заказа"
        verbose_name_plural = "Статусы заказов"


class Order(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.DO_NOTHING)
    total_amount = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Итоговая цена', default=0)
    customer_name = models.CharField(max_length=64, blank=True, null=True, default=None, verbose_name='Имя')
    customer_email = models.EmailField(blank=True, null=True, default=None , verbose_name='Email')
    customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None, verbose_name='Номер телефона')
    customer_address = models.CharField(max_length=128, blank=True, null=True, default=None, verbose_name='Адрес')
    comments = models.TextField(blank=True, null=True, default=None, verbose_name='Комментарий')
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING, verbose_name='Статус')
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f"Заказ {self.id} {self.status.name}"
    
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)


class ProductionInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.DO_NOTHING, verbose_name='Заказ')
    product = models.ForeignKey(Production, blank=True, null=True, default=None, on_delete=models.DO_NOTHING, verbose_name='Имя продукта')
    nmb = models.IntegerField(default=1, verbose_name='Кол-во')
    price_pre_item = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Цена', default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Итоговая цена', default=0)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f"{self.product.title}"
    
    class Meta:
        verbose_name = "Товар в заказе"
        verbose_name_plural = "Товары в заказе"

    def save(self, *args, **kwargs):
        price_pre_item = self.product.price
        self.price_pre_item = price_pre_item
        print(self.nmb)

        self.total_price = int(self.nmb) * price_pre_item

        super(ProductionInOrder, self).save(*args, **kwargs)


#@disable_for_loaddata
def product_in_order_post_save(sender, instance, created, **kwargs):
    order = instance.order
    all_products_in_order = ProductionInOrder.objects.filter(order=order, is_active=True)

    order_total_price = 0
    for item in all_products_in_order:
        order_total_price += item.total_price

    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)

post_save.connect(product_in_order_post_save, sender=ProductionInOrder)


class ProductionInBasket(models.Model):
    session_key = models.CharField(max_length=128, blank=True, null=True, default=None)
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.DO_NOTHING, verbose_name='Заказ')
    product = models.ForeignKey(Production, blank=True, null=True, default=None, on_delete=models.DO_NOTHING, verbose_name='Имя продукта')
    nmb = models.IntegerField(default=1, verbose_name='Кол-во')
    price_pre_item = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Цена', default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Итоговая цена', default=0)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f"{self.product.title}"

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'

    def save(self, *args, **kwargs):
        price_pre_item = self.product.price
        self.price_pre_item = price_pre_item
        self.total_price = int(self.nmb) * price_pre_item

        super(ProductionInBasket, self).save(*args, **kwargs)