# Generated by Django 4.2.5 on 2023-09-24 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_order_zipcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(blank=True, choices=[('0', 'استان خود را انتخاب کنید'), ('1', 'آذربایجان شرقی'), ('2', 'آذربایجان غربی'), ('3', 'اردبیل'), ('4', 'اصفهان'), ('5', 'البرز'), ('6', 'ایلام'), ('7', 'بوشهر'), ('8', 'تهران'), ('9', 'چهارمحال و بختیاری'), ('10', 'خراسان جنوبی'), ('11', 'خراسان رضوی'), ('12', 'خراسان شمالی'), ('13', 'خوزستان'), ('14', 'زنجان'), ('15', 'سمنان'), ('16', 'سیستان و بلوچستان'), ('17', 'فارس'), ('18', 'قزوین'), ('19', 'قم'), ('20', 'کردستان'), ('21', 'کرمان'), ('22', 'کرمانشاه'), ('23', 'کهگیلویه وبویراحمد'), ('24', 'گلستان'), ('25', 'گیلان'), ('26', 'لرستان'), ('27', 'مازندران'), ('28', 'مرکزی'), ('29', 'هرمزگان'), ('30', 'همدان'), ('31', 'یزد')], default='0', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='fulladdress',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='zipcode',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
