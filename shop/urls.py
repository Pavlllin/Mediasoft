from django.urls import include, path
from shop.views import ShopListView


urlpatterns = [
    path('shop/',ShopListView.as_view()),
]
