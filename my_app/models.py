from django.db import models


class User(models.Model):
    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)
    UserName = models.CharField(max_length=200)
    Password = models.CharField(max_length=200)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    UpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.FirstName


class Client(models.Model):
    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)
    CarModel = models.CharField(max_length=100)
    CarNumber = models.CharField(max_length=100)
    PhoneNumber = models.CharField(max_length=100, unique=True)
    CreatedUserId = models.ForeignKey(User, blank=False, null=True, on_delete=models.SET_NULL)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    UpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.FirstName
