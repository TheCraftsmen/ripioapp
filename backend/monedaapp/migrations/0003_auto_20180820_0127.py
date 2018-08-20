# Generated by Django 2.1 on 2018-08-20 01:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monedaapp', '0002_auto_20180819_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchangerow',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transfers', to=settings.AUTH_USER_MODEL),
        ),
    ]
