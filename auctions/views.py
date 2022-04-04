from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import *
from .forms import ListingForm


def index(request):
    listings = AuctionListings.objects.all()
    return render(request, "auctions/index.html", {'listings': listings})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def create(request):
    form = ListingForm()
    if request.method == "POST":
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.creator = request.user
            form.save()
            return redirect('index')

    return render(request, 'auctions/create_listing.html', {'form': form})


def listing_page(request, pk):
    listing = AuctionListings.objects.get(id=pk)
    if request.method == 'POST':
        new_bid = request.POST.get('bid')
        if int(new_bid) > listing.prices:
            listing.bid_author = request.user.username
            listing.prices = new_bid
            listing.save()
    return render(request, 'auctions/listing.html', {'listing': listing})


def close_bid(request, pk):
    listing = AuctionListings.objects.get(id=pk)
    listing.close_bid = True
    listing.save()
    return redirect('listing', pk)


def get_watch_list(request, pk):
    user = User.objects.get(id=request.user.id)
    if user.watchlist is None:
        user.watchlist = pk
        user.save()
        return redirect('listing', pk)
    elif len(list(user.watchlist)) > 1:
        watchlist = list(user.watchlist.split(','))
        if pk not in watchlist:
            watchlist.append(pk)
            user.watchlist = ','.join(watchlist)
            user.save()
        return redirect('listing', pk)

    elif len(list(user.watchlist)) == 1:
        watchlist = list(user.watchlist)
        if pk not in watchlist:
            watchlist.append(pk)
            user.watchlist = ','.join(watchlist)
            user.save()
        return redirect('listing', pk)


def user_watchlist(request):
    user = User.objects.get(id=request.user.id)
    if user.watchlist is None:
        pass
        listings = []
        return render(request, 'auctions/watchlist.html', {'listings': listings})
    elif len(list(user.watchlist)) > 1:
        watchlist = list(user.watchlist.split(','))
        listings = []
        for i in watchlist:
            listings.append(AuctionListings.objects.get(id=i))
        return render(request, 'auctions/watchlist.html', {'listings': listings})
    elif len(list(user.watchlist)) == 1:
        watchlist = list(user.watchlist)
        listings = []
        for i in watchlist:
            listings.append(AuctionListings.objects.get(id=i))
        return render(request, 'auctions/watchlist.html', {'listings': listings})
