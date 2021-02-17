from django_filters import rest_framework as filters
from shop.models import Shop
from city.models import City,Street



class ShopFilter(filters.FilterSet):
    street = filters.CharFilter(field_name = 'street_id__title')
    city = filters.CharFilter(field_name = 'city_id__title')
    class Meta:
        model = Shop
        fields = ['street','city','open_time','close_time']
