from django.db import models

# Create your models here.

class Mysite(models.Model):
    boolChoice = ("Male", "Female")
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    dob = models.DateField()
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    password = models.CharField(max_length=16)

    def __str__(self):
        return self.fname+" "+self.lname