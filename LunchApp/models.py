from django.db import models

# Create your models here.

class Roles(models.Model):
    roleName = models.CharField(max_length=50)

class Users(models.Model):
    document = models.CharField(max_length=15)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    userName = models.CharField(max_length=30)
    password = models.CharField(max_length=255)
    userPhoto = models.CharField(max_length=255)
    rol = models.ForeignKey(Roles, on_delete=models.CASCADE)

class Restaurants(models.Model):
    identifier = models.CharField(max_length=15)
    attendant = models.CharField(max_length=100)

class Products(models.Model):
    productName = models.CharField(max_length=50)
    amount = models.IntegerField()
    purchaseDate = models.TimeField()
    expirationDate = models.DateField()
    productType = models.CharField(max_length=40)
    restaurant = models.ForeignKey(Restaurants, on_delete=models.CASCADE)

class Diets(models.Model):
    diet = models.CharField(max_length=255)
    specifications = models.TextField()
    product = models.ManyToManyField(Products)

class Students(models.Model):
    typeDocument = models.CharField(max_length=5)
    document = models.CharField(max_length=15)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    birthDate = models.DateField()
    age = models.CharField(max_length=3)
    course = models.CharField(max_length=6)
    status = models.CharField(max_length=20)
    admissionDate = models.TimeField()
    userPhoto = models.CharField(max_length=255)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    diet = models.ForeignKey(Diets, on_delete=models.CASCADE)

class Recognition(models.Model):
    creationDate = models.TimeField()
    biometrics = models.CharField(max_length=40)
    student = models.ManyToManyField(Students)
