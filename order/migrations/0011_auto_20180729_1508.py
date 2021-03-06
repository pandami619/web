# Generated by Django 2.0.5 on 2018-07-29 12:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_auto_20180729_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='order.Status', verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='productioninbasket',
            name='nmb',
            field=models.IntegerField(default=1, verbose_name='Кол-во'),
        ),
        migrations.AlterField(
            model_name='productioninbasket',
            name='order',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='order.Order', verbose_name='Заказ'),
        ),
        migrations.AlterField(
            model_name='productioninbasket',
            name='product',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='production.Production', verbose_name='Имя продукта'),
        ),
        migrations.AlterField(
            model_name='productioninorder',
            name='order',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='order.Order', verbose_name='Заказ'),
        ),
        migrations.AlterField(
            model_name='productioninorder',
            name='product',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='production.Production', verbose_name='Имя продукта'),
        ),
    ]
