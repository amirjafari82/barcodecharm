# Generated by Django 4.2.5 on 2023-09-23 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(allow_unicode=True, auto_created=True, unique=True),
        ),
    ]
