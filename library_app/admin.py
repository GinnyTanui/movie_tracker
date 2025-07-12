from django.contrib import admin
from .models import Movie
# Register your models here. 
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'genre', 'rating', 'released_date')  
    search_fields = ('title', 'director')  
    list_filter = ('genre', 'rating')  

admin.site.register(Movie, MovieAdmin)
