from rest_framework import serializers
from shop.models import Shop
from city.models import City,Street
from city.serializers import CitySerializer,StreetSerializer

class ShopSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    street = StreetSerializer()
    class Meta:
        model = Shop
        fields = "__all__"

class ShopCreateSerializer(serializers.ModelSerializer):
    city = serializers.SlugRelatedField(slug_field='title',queryset = City.objects.all())
    class Meta:
        model = Shop
        fields = "__all__"

    def validate(self,data):
        city = data['city']
        street = data['street']
        if city.id != street.city_id:
            raise serializers.ValidationError("Этой улицы нет в этом городе")
        return data
