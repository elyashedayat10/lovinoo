# Generated by Django 3.2.14 on 2022-08-04 07:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('financial', '0006_payhistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='payhistory',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='payhistory',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='payhistory',
            name='tariff',
            field=models.CharField(max_length=125),
        ),
    ]
