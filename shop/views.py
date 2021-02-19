from django.db.models import Q
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.response import Response

from shop.models import Shop
from shop.serializers import ShopCreateSerializer, ShopSerializer
from shop.service import ShopFilter


class ShopListView(generics.ListAPIView, generics.CreateAPIView):
    filter_backend = [DjangoFilterBackend]
    serializer_class = ShopSerializer
    filterset_class = ShopFilter

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ShopCreateSerializer
        return ShopSerializer

    def get_queryset(self):
        is_open = self.request.query_params.get('open', None)
        shop = Shop.objects.filter()
        time_server = timezone.localtime(timezone.now())
        if not is_open: return shop
        if is_open == "1":
            shop = shop.filter(Q(open_time__lte=time_server.strftime('%H:%M')),
                               Q(close_time__gt=time_server.strftime('%H:%M')))
        elif is_open == "0":
            shop = shop.filter(Q(open_time__gt=time_server.strftime('%H:%M'))
                               | Q(close_time__lte=time_server.strftime('%H:%M')))
        return shop

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.object = serializer.save()
            headers = self.get_success_headers(serializer.data)
            print(serializer.data)
            return Response(serializer.data['id'], status=201,
                            headers=headers)

        return Response(serializer.errors, status=400)
