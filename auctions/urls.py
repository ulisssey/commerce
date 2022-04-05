from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("listing/<str:pk>", views.listing_page, name='listing'),
    path("get_bid/<str:pk>", views.get_bid, name='get_bid'),
    path("get_comment/<str:pk>", views.get_comment, name='comment'),
    path("watchlist/<str:pk>", views.get_watch_list, name="watchlist"),
    path("watchlist", views.user_watchlist, name='user_watchlist'),
    path("close_bid/<str:pk>", views.close_bid, name='close')
]
