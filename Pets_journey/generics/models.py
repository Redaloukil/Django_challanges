from django.db import models


class BaseModel(models.Model):
    published_at = models.DateField()
    updated_at = models.DateField()