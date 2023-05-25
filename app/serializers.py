from rest_framework import serializers
from .models import IMDB

class IMDBSerializer(serializers.ModelSerializer):
    class Meta:
        model = IMDB
        fields = '__all__'