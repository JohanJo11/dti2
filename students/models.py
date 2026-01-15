from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    phone_number = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} , {self.last_name} , {self.age} , {self.phone_number}"


class Team(models.Model):
    name = models.CharField(max_length=255)
    league = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255,default="unknown")
    ranking = models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.nationality}"

class Nationality(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"

        
class Footballer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    #nationality = models.ForeignKey(Nationality, on_delete=models.CASCADE , related_name='footballers',null=True,blank=True)
    position = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='footballers',null=True,blank=True)
    image_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} , {self.last_name} , {self.team}"
    
class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.price} dollars"
    

    
    

