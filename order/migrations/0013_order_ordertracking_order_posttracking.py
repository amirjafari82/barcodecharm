# Generated by Django 4.2.5 on 2023-09-25 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0012_remove_order_delivered'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='ordertracking',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='posttracking',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
