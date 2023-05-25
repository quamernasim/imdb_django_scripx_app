from django.contrib import admin
from .models import IMDB

# Register your models here.

@admin.register(IMDB)
class IMDBAdmin(admin.ModelAdmin):

    list_display = ('imdb_title_id', 'original_title', 
                    'year', 'date_published', 'genre', 'duration', 
                    'language', 'description', 'reviews_from_users', 'reviews_from_critics')
