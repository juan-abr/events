from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

# Create your views here.
def index(request, year, month):
    # t = date.today()
    # month = date.strftime(t, '%b')
    # year = t.year
    title = "CMMA Event Calendar - %s %s" % (month, year)
    return HttpResponse("<h1>%s</h1>" % title)