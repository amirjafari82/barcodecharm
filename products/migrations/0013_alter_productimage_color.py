# Generated by Django 4.2.5 on 2023-09-22 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_alter_productimage_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='color',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]
