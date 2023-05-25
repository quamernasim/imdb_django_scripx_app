from django.shortcuts import render
from django.views import View
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


from .models import IMDB
from .serializers import IMDBSerializer


# Create your views here.

class IMDBView(View):
    def get(self, request):
        imdb = IMDB.objects.all()
        return render(request, "app/allrecords.html", locals())
    
@api_view(['GET'])
def filter(request):
    if request.method == "GET":
        genre = request.GET.get('genre')
        language = request.GET.get('lang')
        if genre:
            data = filter_by_genre(genre)
            return Response(data)
        elif language:
            data = filter_by_language(language)
            return Response(data)
        else:
            data = {
                "message": "Please provide a genre or language",
                "status": status.HTTP_400_BAD_REQUEST
            }
            return Response(data)

def filter_by_genre(genre):
    if genre.lower() == "none":
        imdb = IMDB.objects.filter(genre__isnull=True)
    else:
        imdb = IMDB.objects.filter(genre__icontains=genre)
    if imdb.exists():
        imdb_serializer = IMDBSerializer(imdb, many=True)
        data = {
            "message": "Records found for genre: {}".format(genre),
            "status": status.HTTP_200_OK,
            "data": imdb_serializer.data
        }
        return data
    else:
        data = {
            "message": "No records found for genre: {}".format(genre),
            "status": status.HTTP_404_NOT_FOUND
        }
        return data
        
def filter_by_language(language):
    if language.lower() == "none":
        imdb = IMDB.objects.filter(language__isnull=True)
    else:
        imdb = IMDB.objects.filter(language__icontains=language)
    if imdb.exists():
        imdb_serializer = IMDBSerializer(imdb, many=True)
        data = {
            "message": "Records found for language: {}".format(language),
            "status": status.HTTP_200_OK,
            "data": imdb_serializer.data
        }
        return data
    else:
        data = {
            "message": "No records found for language: {}".format(language),
            "status": status.HTTP_404_NOT_FOUND
        }
        return data