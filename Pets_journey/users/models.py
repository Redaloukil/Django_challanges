from django.db import models
from django.contrib.auth.models import AbstractUser , PermissionsMixin
from users.managers import UserManager
# Create your models here.

class User(AbstractUser):
    username = models.CharField(unique=True , max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    
    objects = UserManager()
    
    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['first_name' ,'last_name',]

    class Meta:
        app_label = 'users'

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def save(self, *args, **kwargs):
        if not self.password:
            self.password = str(uuid.uuid4()).replace('-', '')
        super(User, self).save(*args, **kwargs)

    


