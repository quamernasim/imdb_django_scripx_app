from django.db import models

# Create your models here.

class IMDB(models.Model):
    #make imdb_title_id as primary key
    imdb_title_id = models.IntegerField(primary_key=True)
    original_title = models.CharField(max_length=100)
    year = models.IntegerField()
    date_published = models.DateField()
    genre = models.CharField(max_length=50)
    duration = models.IntegerField()
    language = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    reviews_from_users = models.IntegerField()
    reviews_from_critics = models.IntegerField()

    def __str__(self):
        return self.original_title
    
