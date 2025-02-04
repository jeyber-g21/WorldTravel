from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_user, name="login"), 
    path("logout", views.logout_view, name="logout"),
    path("register", views.register_user, name="register"),
    path("send_email", views.email, name="email"),
    path("destination/", views.trips, name="trips"),
    path("travel/details/<int:id>", views.travel, name="travel"),
    path("remove_watchlist/<int:id>", views.remove, name="removewatchlist"),
    path("add_watchlist/<int:id>", views.add, name="addwatchlist"),
    path("wishlist", views.wishlist, name="wishlist"),
    path("mybooking", views.mybooking, name="mybooking"),
    path("booking/<int:id>", views.booking, name="booking"),
    path("deals", views.deals, name="deals"),
]