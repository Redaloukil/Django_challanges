from django.db import models
from owners.models import Owner


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
    owner = models.ForeignKey(Owner , on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    birth_day = models.DateField()

class Cat(Pet):
    pass

class Dog(Pet):
    pass