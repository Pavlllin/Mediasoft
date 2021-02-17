from rest_framework import serializers
from city.models import City, Street


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('title',)

class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = ('title',)
