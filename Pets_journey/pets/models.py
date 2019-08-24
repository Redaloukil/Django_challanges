from django.db import models
from users.models import User

from datetime import datetime    


# Create your models here.
CAT = (
    ('0' , 'type0'),
    ('1' , 'type1'),
)

DOG = (
    ('0' , 'type0'),
    ('1' , 'type1'),
)
class Pet(models.Model):
    owner = models.ForeignKey(User , on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=False, blank=True)
    

class Cat(Pet):
    def __str__(self):
        return self.name + ' ' + self.owner.username

class Dog(Pet):
    def __str__(self):
        return self.name + ' ' + self.owner.username