from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from python_shop.views import ClientProfileView, ShopView, BasketView

router = DefaultRouter()
router.register(r'profile', ClientProfileView)
router.register(r'shop', ShopView)
router.register(r'cart', BasketView)
urlpatterns = [
    # Endpoints:
    url(r'', include(router.urls))
]

