# Generated by Django 2.0.5 on 2018-07-29 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0014_auto_20180729_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productionimage',
            name='product',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='production.Production'),
        ),
    ]
