# Generated by Django 3.2.5 on 2022-04-03 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_alter_auctionlistings_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlistings',
            name='image',
            field=models.ImageField(blank=True, default='0.jpg', upload_to='images/'),
        ),
    ]
