from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from city.models import City,Street
from city.serializers import CitySerializer, StreetSerializer

class CityListView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class StreetListView(generics.ListAPIView):
    queryset = Street.objects.filter()
    serializer_class = StreetSerializer
    def get_queryset(self):
        id_city = self.kwargs['city_id']
        streets = Street.objects.filter(city_id = id_city)
        return streets
