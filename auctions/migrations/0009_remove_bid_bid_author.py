# Generated by Django 3.2.5 on 2022-04-02 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_alter_bid_bid_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='bid_author',
        ),
    ]