# Generated by Django 4.2.5 on 2023-09-22 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_rename_color_product_colors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='color',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
