from django.contrib import admin

from .models import Location, Attendee, Event

# Register your models here.
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display    = ('name', 'address', 'phone')
    ordering        = ('name',)
    search_fields   = ('name', 'address')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    # fields          = (('name', 'location'), 'event_date', 'description', 'instructor')
    fieldsets          = (
        ('Required Information', {
            'description': "These fields are required for each event.",
            'fields': (('name', 'location'), 'event_date')
        }),
        ('Optional Information', {
            'classes': ('collapse',),
            'fields': ('description', 'instructor')
        }),
    )
    list_display    = ('name', 'event_date', 'location')
    list_filter     = ('event_date', 'location')
    ordering        = ('-event_date',)

# admin.site.register(Location)
admin.site.register(Attendee)
# admin.site.register(Event)