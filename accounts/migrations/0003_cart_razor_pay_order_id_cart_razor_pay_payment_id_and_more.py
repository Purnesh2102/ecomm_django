# Generated by Django 4.1.6 on 2023-02-16 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_cart_cartitems'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='razor_pay_order_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='razor_pay_payment_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='razor_pay_payment_signature',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
