# Generated by Django 4.2.5 on 2023-09-23 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_alter_productimage_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='peresentimage',
            field=models.ImageField(default=None, upload_to='static/images/products'),
        ),
    ]