from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Continents(models.Model):
    continent = models.CharField(max_length=50)
   

    def __str__(self):
        return self.continent
    
class Month(models.Model):
    month_departure = models.CharField(max_length=50, null=True)
   

    def __str__(self):
        return self.month_departure

class Booking(models.Model):
    month_trip = models.CharField(max_length=900,null=True)
    user_trip = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="user_trip")
   

    def __str__(self): 
       return f"{self.user_trip} travels in {self.month_trip}"

    
class Travel(models.Model):
    title = models.CharField(max_length=64)
    description1 = models.CharField(max_length=900)
    description2 = models.CharField(max_length=900)
    description3 = models.CharField(max_length=900)
    short_description = models.CharField(max_length=900,null=True)
    description4 = models.CharField(max_length=900,null=True)
    description5 = models.CharField(max_length=900,null=True)
    description6 = models.CharField(max_length=900,null=True)
    description7 = models.CharField(max_length=900,null=True)
    description8 = models.CharField(max_length=900,null=True)
    description9 = models.CharField(max_length=900,null=True)
    image1 = models.CharField(max_length=900)
    image2 = models.CharField(max_length=900)
    image3 = models.CharField(max_length=900)
    image4 = models.CharField(max_length=900)
    image5 = models.CharField(max_length=900,null=True)
    image6 = models.CharField(max_length=900,null=True)
    image7 = models.CharField(max_length=900,null=True)
    image8 = models.CharField(max_length=900,null=True)
    price = models.FloatField(default=0)
    isActive = models.BooleanField(default=True)
    booking_user = models.ManyToManyField(User,  blank=True, null=True, related_name="BOOKED")
    place = models.ForeignKey(Continents, on_delete=models.CASCADE, null=True, blank=True, related_name="site")
    time = models.ManyToManyField(Month,  blank=True, null=True, related_name="date")
    watchlist = models.ManyToManyField(User, blank=True, null=True, related_name="listingwatchlist")
    def __str__(self):
        return self.title