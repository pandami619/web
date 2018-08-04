# Generated by Django 2.0.4 on 2018-07-09 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0012_productionimage_is_main'),
        ('order', '0004_auto_20180709_0010'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductionInBasket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nmb', models.IntegerField(default=1)),
                ('price_pre_item', models.DecimalField(decimal_places=0, default='0', max_digits=10, verbose_name='Цена')),
                ('total_price', models.DecimalField(decimal_places=0, default='0', max_digits=10, verbose_name='Итоговая цена')),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='order.Order')),
                ('product', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='production.Production')),
            ],
            options={
                'verbose_name': 'Товар в корзине',
                'verbose_name_plural': 'Товары в корзине',
            },
        ),
        migrations.AddField(
            model_name='productioninorder',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]