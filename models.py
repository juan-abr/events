from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class LocationManager(models.Manager):
    def get_queryset(self):
        return super(LocationManager, self).get_queryset().filter(zip_code='21704')

class Location(models.Model):
    name            = models.CharField('Location Name', max_length = 120)
    address         = models.CharField(max_length = 300)
    zip_code        = models.CharField('Zip/Post Code', max_length = 12)
    phone           = models.CharField('Contact Phone', max_length = 20, blank = True)
    web             = models.URLField('Web Address', blank = True)
    email_address   = models.EmailField('Email Address', blank = True)

    locations = models.Manager()
    local_locations = LocationManager()

    def __str__(self):
        return self.name



class Attendee(models.Model):
    first_name  = models.CharField(max_length = 30)
    last_name   = models.CharField(max_length = 30)
    email       = models.EmailField('Attendee Email')

    def __str__(self):
        return self.first_name + " " + self.last_name


class EventManager(models.Manager):
    def event_type_count(self, event_type):
        return self.filter(name__icontains=event_type).count()


class Event(models.Model):
    name        = models.CharField('Event Name', max_length = 120)
    event_date  = models.DateTimeField('Event Date')
    location    = models.ForeignKey(Location, blank=True, null=True, on_delete=models.CASCADE)
    # instructor  = models.CharField(max_length = 60)
    instructor  = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    attendees   = models.ManyToManyField(Attendee, blank=True)
    description = models.TextField(blank = True)
    events = EventManager()

    def save(self, *args, **kwargs):
        self.manager = User.objects.get(username = 'admin') # User 'admin' must exist
        super(Event, self).save(*args, **kwargs)

    def event_timing(self, date):
        if self.event_date > date:
            return "Event is after this date"
        elif self.event_date == date:
            return "Event is on the same day"
        else:
            return "Event is before this date"
    
    @property
    def name_slug(self):
        return self.name.lower().replace(' ','-')

    def __str__(self):
        return self.name