from django.db import models
from time import time

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=50)


