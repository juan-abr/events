from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from datetime import date
import calendar
from calendar import HTMLCalendar

from .models import Event
from .forms import LocationForm

# Create your views here.
def index(request, year = date.today().year, month = date.today().month):
    # t = date.today()
    # month = date.strftime(t, '%b')
    # year = t.year
    year = int(year)
    month = int(month)
    if year < 2000 or year > 2099: year = date.today().year
    month_name = calendar.month_name[month]
    title = "CMMA Event Calendar - %s %s" % (month_name, year)
    cal = HTMLCalendar().formatmonth(year, month)
    announcements = [
        {
            'date': '6-10-2020',
            'announcement': "Registrations Open"
        },
        {
            'date': '6-15-2020',
            'announcement': "Website accessible online."
        }
    ]
    # return HttpResponse("<h1>%s</h1><p>%s</p>" % (title, cal))
    return render(request,
        'events/calendar_base.html',
        {'title': title, 'cal': cal, 'announcements': announcements}
    )

def all_events(request):
    event_list = Event.objects.all()
    return render(request,
        'events/event_list.html',
        {'event_list': event_list}
    )

def add_location(request):
    submitted = False
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_location/?submitted=True')
    else:
        form = LocationForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'events/add_location.html', {'form': form, 'submitted': submitted})