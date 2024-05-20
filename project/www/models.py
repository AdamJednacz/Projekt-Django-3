from django.db import models

class Club(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField(max_length=10)
    photo = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name 


    

class Position(models.Model):
    name = models.CharField(max_length=10)
 

    def __str__(self):
        return self.name
    


class Player(models.Model):
    name = models.CharField(max_length=10)
    surname = models.CharField(max_length=15)
    age = models.CharField(max_length=10)
    club = models.ManyToManyField(Club)
    position = models.ManyToManyField(Position)
    photo = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name + " " + self.surname   
    
