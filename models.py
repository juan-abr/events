from django.db import models

# Create your models here.
class Location(models.Model):
    name            = models.CharField('Location Name', max_length = 120)
    address         = models.CharField(max_length = 300)
    zip_code        = models.CharField('Zip/Post Code', max_length = 12)
    phone           = models.CharField('Contact Phone', max_length = 20, blank = True)
    web             = models.URLField('Web Address', blank = True)
    email_address   = models.EmailField('Email Address', blank = True)

    def __str__(self):
        return self.name


class Attendee(models.Model):
    first_name  = models.CharField(max_length = 30)
    last_name   = models.CharField(max_length = 30)
    email       = models.EmailField('Attendee Email')

    def __str__(self):
        return self.first_name + " " + self.last_name


class Event(models.Model):
    name        = models.CharField('Event Name', max_length = 120)
    event_date  = models.DateTimeField('Event Date')
    location    = models.ForeignKey(Location, blank=True, null=True, on_delete=models.CASCADE)
    instructor  = models.CharField(max_length = 60)
    attendees   = models.ManyToManyField(Attendee, blank=True)
    description = models.TextField(blank = True)

    def __str__(self):
        return self.name