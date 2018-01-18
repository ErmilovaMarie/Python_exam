from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.viewsets import GenericViewSet, mixins
from rest_framework.permissions import IsAuthenticated
from .models import Shop_Client, Items_options, Basket
from .serializers import (ClientProfileSerializer, ShopSerializer, ClientBasketSerializer,)


# Create your views here.


class ClientProfileView(GenericViewSet,     # ProfileView = ClientProfileView
                  mixins.ListModelMixin,  # TODO: remove after tests are completed
                  mixins.CreateModelMixin):
    serializer_class = ClientProfileSerializer   # ProfileSerializer = ClientProfileSerializer
    queryset = Shop_Client.objects.all()


class ShopView(GenericViewSet,
               mixins.ListModelMixin):
    serializer_class = ShopSerializer
    queryset = Items_options.objects.all()


class BasketView(GenericViewSet,
               mixins.ListModelMixin,
               mixins.CreateModelMixin):
    serializer_class = ClientBasketSerializer
    queryset = Basket.objects.all()
