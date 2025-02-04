from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django .core.mail import EmailMessage
# from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages
from .models import Continents,Travel,Month,Booking
from .models import User



def index(request):
     continents= Continents.objects.all()
     travel= Travel.objects.all()
     return render(request, "finalproject/index.html",{
        "continents": continents,
        "travel":travel
     })

def login_user(request):
     if request.method == "POST":
      username = request.POST["username"]
      password = request.POST["password"]
      user = authenticate(request, username=username, password=password)
      if user is not None:
          login(request, user)
          return HttpResponseRedirect(reverse("index"))
          ...
      else:
          return render(request, "finalproject/login.html", {
                    "message": "Invalid username and/or password."
               })
     else:

      return render(request, 'finalproject/login.html')
     
def logout_view(request):
   logout(request)
   return HttpResponseRedirect(reverse("index"))

def register_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "finalproject/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "finalproject/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "finalproject/register.html")


def email(request):
   
   if request.method == "POST":
      name = request.POST['name']
      email = request.POST['email']
      message = request.POST['message']
      

      email = EmailMessage("mensaje django",
            "{} con gmail {} has sent this email:\n\n {}".format(name,email,message),
         
         settings.EMAIL_HOST_USER,
         ['gomezjeyber@gmail.com']
      )
      email.fail_silently = False
      email.send()

      messages.success(request, 'email has been requested')
      return redirect ('index')
   
def trips (request):
   if request.method=="POST":
        
        continentindex=request.POST['continent']
        monthindex=request.POST['month']
        continent=Continents.objects.get(continent=continentindex)
        monthindex1=Month.objects.get(month_departure=monthindex)
        active=Travel.objects.filter(isActive=True, place=continent,time=monthindex1)
        
        if len(active) != 0:
            isFollowing=True
            continents= Continents.objects.all()
            return render(request, "finalproject/destination.html",{
               "travel": active,
               "continents":continents
             })
        else:
            isFollowing=False
            continents= Continents.objects.all()
            return render(request, "finalproject/destination.html",{
               "travel": active,
               "message": "No available trips for that month, sorry",
               "continents":continents
             })
   else:
       continents= Continents.objects.all()
       active=Travel.objects.all()
       return render(request, "finalproject/destination.html",{
               "travel": active,
               "continents":continents
             })

def travel (request,id):
       
       travel2=Travel.objects.filter(isActive=True, pk=id)
       travel3=Travel.objects.get(isActive=True, pk=id)
       listwatchlist = request.user in travel3.watchlist.all()
       return render(request, "finalproject/details.html",{
        "travel": travel2,
        "listwatchlist":listwatchlist,
        
    })    

def remove (request,id):
       
    travel2=Travel.objects.get(pk=id)
    currentuser=request.user
    travel2.watchlist.remove(currentuser)
    return HttpResponseRedirect(reverse("travel",args=(id, )))

def add (request,id):
       
    travel2=Travel.objects.get(pk=id)
    currentuser=request.user
    travel2.watchlist.add(currentuser)
    return HttpResponseRedirect(reverse("travel",args=(id, )))

def wishlist(request):
    currentuser=request.user
    travel2=Travel.objects.filter(watchlist=currentuser)
    if len(travel2) != 0:
            return render(request, "finalproject/wishlist.html",{
            "travel": travel2,
            
            })
    else:
            return render(request, "finalproject/wishlist.html",{
            "travel": travel2,
            "message": "The wishlist is empty"
            })

def booking(request,id):
    if request.method=="POST":
        
        monthindex=request.POST['exact_month']
        travel2=Travel.objects.get(pk=id)
        currentuser=request.user
        travel2.booking_user.add(currentuser)
        newbooking=Booking(
        month_trip=monthindex,user_trip=currentuser,
    )
        newbooking.save()
        return HttpResponseRedirect(reverse("travel",args=(id, )))
    
def mybooking(request):
    currentuser=request.user
    travel2=Travel.objects.filter(booking_user=currentuser)
    month_booked =Booking.objects.filter(user_trip=currentuser)
    if len(travel2) != 0:
            return render(request, "finalproject/mybooking.html",{
            "travel": travel2,
            "month_booked":month_booked
            
            })
    else:
            return render(request, "finalproject/mybooking.html",{
            "travel": travel2,
            "message": "Not booking, select any trip to make a booking",
            
            })

def deals (request):
       return render(request, "finalproject/deals.html",{
            "message": "Not deals available right now"
            
            }) 