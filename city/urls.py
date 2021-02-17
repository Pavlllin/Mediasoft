from django.urls import include, path
from city.views import CityListView,StreetListView

urlpatterns = [
    path('city/',CityListView.as_view()),
    path('<int:city_id>/street/',StreetListView.as_view()),
]
