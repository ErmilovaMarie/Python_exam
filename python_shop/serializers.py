from django.shortcuts import get_object_or_404
from rest_framework import serializers
import jwt
from rest_framework_jwt.serializers import jwt_payload_handler
from Code import settings
from python_shop.models import Shop_Client, Items_options, Basket


class ClientProfileSerializer(serializers.ModelSerializer):     # ProfileSerializer = ClientProfileSerializer
    password = serializers.CharField(write_only=True)
    cart = serializers.IntegerField(write_only=True, default="")
    token = serializers.SerializerMethodField()

    class Meta:
        model = Shop_Client
        fields = (
            'token',
            'email',
            'user',     # username = user
            'password',
            'basket',
        )

    def create_user(self, validated_data):
        user = Shop_Client(email=validated_data['email'], username=validated_data['user'])
        user.set_password(validated_data['password'])
        user.save()
        if validated_data['basket'] != "":
            basket = get_object_or_404(Basket, id=validated_data['cart'])
            basket.customer = user
        return user

    def get_token(self, obj):
        payload = jwt_payload_handler(obj)
        token = jwt.encode(payload, settings.SECRET_KEY)
        return token.decode('unicode_escape')


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items_options
        fields = (
            'id',
            '__str__',
            'description',
            'price',
        )


class ClientBasketSerializer(serializers.ModelSerializer):
    last_cart = serializers.IntegerField(write_only=True, default="")
    customer_email = serializers.EmailField(write_only=True, default="")

    class Meta:
        model = Basket
        fields = (
            'id',
            'last_basket',
            'customer_email',
            'items',
        )

    def create(self, validated_data):
        if validated_data['last_basket'] != "":
            last_cart = get_object_or_404(Basket, id=validated_data['last_basket'])
            for good in validated_data['items']:
                last_cart.goods.add(good)
            last_cart.save()
            return last_cart

        if validated_data['customer_email'] != "":
            client = Shop_Client.objects.filter(email=validated_data['customer_email']).first()
        else:
            client = Shop_Client()
            client.save(

            )
        user_basket = Basket(customer=client)
        user_basket.save()
        user_basket.items = validated_data['items']
        user_basket.save()
        return user_basket

