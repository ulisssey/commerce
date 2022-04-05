from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    watchlist = models.CharField(max_length=100, null=True, blank=True)


class Categories(models.Model):
    category = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.category


class AuctionListings(models.Model):
    image = models.ImageField(upload_to='images/', blank=True, default='images/0.jpg')
    title = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)
    prices = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    bid_author = models.CharField(max_length=20, null=True)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)
    close_bid = models.BooleanField(default=False)


class Bid(models.Model):
    bid = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    listing = models.ForeignKey(AuctionListings, on_delete=models.CASCADE)


class Comments(models.Model):
    listing_id = models.IntegerField(null=True)
    body = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

