# Generated by Django 2.0.5 on 2018-07-30 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0017_auto_20180730_2153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productcategory',
            old_name='name',
            new_name='title',
        ),
    ]
