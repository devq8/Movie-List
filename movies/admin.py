from django.contrib import admin
from movies.models import Movie, List

# Register your models here.
admin.site.register([Movie, List])