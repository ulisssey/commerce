from django.forms import ModelForm
from .models import AuctionListings


class ListingForm(ModelForm):
    class Meta:
        model = AuctionListings
        fields = ['image', 'title', 'description', 'prices']
