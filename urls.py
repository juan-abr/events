from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_location/', views.add_location, name = 'add-location'),
    path('events/', views.all_events, name='show-events'),
    # path('<int:year>/<str:month>/', views.index, name='index'),
    re_path(r'^(?P<year>[0-9]{4})/(?P<month>0?[1-9]|1[0-2])/', views.index, name='index'),
    path('gentext/', views.gen_text, name='generate-text-file'),
    path('gencsv/', views.gen_csv, name='generate-csv-file'),
]