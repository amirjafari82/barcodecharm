# Generated by Django 4.2.5 on 2023-10-21 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_comment_approved'),
        ('order', '0018_remove_order_product_remove_order_productcolor_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderProducts',
            new_name='OrderProduct',
        ),
    ]
