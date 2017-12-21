from django.db import models
import datetime
from django.utils.timezone import utc

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=50)


class Contact(models.Model):
    name = models.CharField(max_length=200, null=True)
    age = models.IntegerField(default=0, null=True)
    email = models.EmailField(null=True)

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)

    def __unicode__(self):
        return self.name


