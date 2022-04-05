from django.contrib import admin
from .models import User, AuctionListings, Bid, Comments

admin.site.register(User)
admin.site.register(AuctionListings)
admin.site.register(Bid)
admin.site.register(Comments)
