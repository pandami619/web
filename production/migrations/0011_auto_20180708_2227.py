# Generated by Django 2.0.4 on 2018-07-08 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0010_auto_20180708_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productionimage',
            name='image',
            field=models.ImageField(upload_to='image'),
        ),
    ]