from django.contrib import admin
from .models import Movies
# Register your models here.
admin.site.register(Movies)
admin.site.site_header = "Welcome to world of Movies"