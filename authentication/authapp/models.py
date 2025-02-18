from django.db import models
from django.contrib.auth.models import User

# Model to represent a service
class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

# Model to represent a form (e.g., user submissions)
class Form(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    fields = models.JSONField()  # For dynamic form fields, use JSON
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Model to represent settings (e.g., application settings)
class Setie(models.Model):
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.key

# Model to represent user profiles (assuming extending User)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username

class Member(models.Model):
    name = models.CharField(max_length=100, null= False, blank=False)
    changamoto = models.CharField(max_length=100, null=True, blank=True)
    Biblia = models.CharField(max_length=100, null=True, blank=True)
    kesha = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(null=True, blank=True)  # Use DateField for actual dates
    lesson = models.CharField(max_length=100, null=True, blank=True)
    deacon = models.CharField(max_length=100, null=True, blank=True)
    nyimbo = models.CharField(max_length=100, null=True, blank=True)
    maombi = models.CharField(max_length=100, null=True, blank=True)
    maombitime = models.CharField(max_length=100, null=True, blank=True)
    ibada = models.CharField(max_length=100, null=True, blank=True)
    jtano = models.CharField(max_length=100, null=True, blank=True)
    ijumaa = models.CharField(max_length=100, null=True, blank=True)
    sabato = models.CharField(max_length=100, null=True, blank=True)
    zaka = models.CharField(max_length=100, null=True, blank=True)
    sadaka = models.CharField(max_length=100, null=True, blank=True)
    makambi = models.CharField(max_length=100, null=True, blank=True)
    michango = models.CharField(max_length=100, null=True, blank=True)
    misaada = models.CharField(max_length=100, null=True, blank=True)
    thamani = models.CharField(max_length=100, null=True, blank=True)
    injili = models.CharField(max_length=100, null=True, blank=True)
    mudawakuhubiri = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"

class DeaconInfo(models.Model):
    name=models.CharField(max_length=100)
    date = models.DateField(null=False, blank=False) 
    jumla=models.CharField(max_length=50,null=False,blank=False)

    def __str__(self):
        return self.name