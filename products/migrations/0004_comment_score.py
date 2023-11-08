# Generated by Django 4.2.5 on 2023-09-20 12:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_slug_alter_product_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='score',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
    ]
