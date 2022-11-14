from rest_framework import serializers
from .models import Song, Artiste

#create a sing serializer
class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = (
            "id",
            "title",
            "date_released",
            "likes",
            "artiste_id",
        )


#Serializer for artiste

class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = (
            "id",
            "first_name",
            "last_name",
            "age"
        )

