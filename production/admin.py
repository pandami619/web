from django.contrib import admin
from .models import Production, ProductionImage


class ProductionImageInline(admin.TabularInline):
    model = ProductionImage
    extra = 0


class ProductionAdmin(admin.ModelAdmin):
    list_dispaly = [field.name for field in Production._meta.fields]
    inlines = [ProductionImageInline]

    class Meta:
        model = Production


admin.site.register(Production, ProductionAdmin)


class ProductionImageAdmin(admin.ModelAdmin):
    list_dispaly = [field.name for field in ProductionImage._meta.fields]

    class Meta:
        model = ProductionImage


admin.site.register(ProductionImage, ProductionImageAdmin)