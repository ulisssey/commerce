# Generated by Django 3.2.5 on 2022-04-02 17:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_bid'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='bid_author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
