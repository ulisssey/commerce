from django.forms import ModelForm
from .models import AuctionListings, Comments


class ListingForm(ModelForm):
    class Meta:
        model = AuctionListings
        fields = ['image', 'title', 'description', 'prices']


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['body']
