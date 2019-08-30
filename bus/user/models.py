from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

# Create your models here.
class user(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    choice = (('Engineering college', 'Engineering college' ),
             ('Dentist college', 'Dentist college'),
             ('commerce college', 'commerce college'),)
    college = MultiSelectField(choices = choice)


    def __str__(self):
        return f'{self.username} user'

class Bus(models.Model):
    bus_number = models.IntegerField()
    bus_direction = models.TextField()
    bus_time = models.TextField()

    def __str__(self):
        return self.bus_direction
