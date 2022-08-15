# Generated by Django 3.2.14 on 2022-08-04 05:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('financial', '0002_cartpay_origincart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartpay',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cart_pay', to=settings.AUTH_USER_MODEL),
        ),
    ]
