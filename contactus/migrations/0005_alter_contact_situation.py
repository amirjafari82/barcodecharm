# Generated by Django 4.2.5 on 2023-09-25 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactus', '0004_alter_contact_situation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='situation',
            field=models.CharField(choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Solved', 'Solved')], default='Pending', max_length=30),
        ),
    ]
