from django.contrib import admin
from .models import *


class ProductionInOrderInline(admin.TabularInline):
    model = ProductionInOrder
    extra = 0


class StatusAdmin(admin.ModelAdmin):
    list_dispaly = [field.name for field in Status._meta.fields]

    class Meta:
        model = Status


admin.site.register(Status, StatusAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_dispaly = [field.name for field in Order._meta.fields]
    inlines = [ProductionInOrderInline]

    class Meta:
        model = Order


admin.site.register(Order, OrderAdmin)


class ProductionInOrderAdmin(admin.ModelAdmin):
    list_dispaly = [field.name for field in ProductionInOrder._meta.fields]

    class Meta:
        model = ProductionInOrder


admin.site.register(ProductionInOrder, ProductionInOrderAdmin)


class ProductionInBasketAdmin(admin.ModelAdmin):
    list_dispaly = [field.name for field in ProductionInBasket._meta.fields]

    class Meta:
        model = ProductionInBasket


admin.site.register(ProductionInBasket, ProductionInBasketAdmin)
