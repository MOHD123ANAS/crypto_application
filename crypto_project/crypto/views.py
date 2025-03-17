from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from .models import Organization, CryptoPrice
from .serializers import OrganizationSerializer, CryptoPriceSerializer


class CryptoPricePagination(PageNumberPagination):
    page_size = 5  # ✅ Number of items per page
    page_size_query_param = 'page_size'
    max_page_size = 10

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated]

class CryptoPriceViewSet(viewsets.ModelViewSet):
    queryset = CryptoPrice.objects.all().order_by('-timestamp')
    serializer_class = CryptoPriceSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CryptoPricePagination

def crypto_prices_page(request):
    return render(request, 'crypto_prices.html')

def crypto_prices_view(request):
    prices = CryptoPrice.objects.all().order_by('-timestamp')[:10]
    return render(request, 'crypto_prices.html', {'prices': prices})
