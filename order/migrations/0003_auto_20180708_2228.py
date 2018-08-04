# Generated by Django 2.0.4 on 2018-07-08 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20180708_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer_address',
            field=models.CharField(blank=True, default=None, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='total_amount',
            field=models.DecimalField(decimal_places=0, default='0', max_digits=10, verbose_name='Цена'),
        ),
        migrations.AddField(
            model_name='productioninorder',
            name='nmb',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='productioninorder',
            name='price_pre_item',
            field=models.DecimalField(decimal_places=0, default='0', max_digits=10, verbose_name='Цена'),
        ),
        migrations.AddField(
            model_name='productioninorder',
            name='total_price',
            field=models.DecimalField(decimal_places=0, default='0', max_digits=10, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_phone',
            field=models.CharField(blank=True, default=None, max_length=48, null=True),
        ),
    ]
