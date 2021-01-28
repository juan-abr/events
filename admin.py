from django.contrib import admin

from .models import Location, Attendee, Event

# Register your models here.
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone')
    ordering = ('name',)
    search_fields = ('name', 'address')

# admin.site.register(Location)
admin.site.register(Attendee)
admin.site.register(Event)