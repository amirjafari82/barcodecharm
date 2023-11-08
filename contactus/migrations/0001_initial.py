# Generated by Django 4.2.5 on 2023-09-20 08:21

from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=30)),
                ('phonenumber', models.CharField(max_length=11)),
                ('title', models.CharField(max_length=50)),
                ('explanation', models.TextField()),
                ('answered', models.BooleanField(default=False)),
                ('created', django_jalali.db.models.jDateTimeField(auto_now_add=True)),
            ],
        ),
    ]