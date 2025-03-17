from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrganizationViewSet, CryptoPriceViewSet,crypto_prices_view,crypto_prices_page

router = DefaultRouter()
router.register(r'organizations', OrganizationViewSet)
router.register(r'crypto-prices', CryptoPriceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('crypto-prices/',crypto_prices_view, name='crypto_prices'),
    path('crypto-prices-ui/', crypto_prices_page, name='crypto_prices_page'),

]