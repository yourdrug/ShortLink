from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from links.models import Links
from links.serializers import LinksSerializer


class BookViewSet(ModelViewSet):
    queryset = Links.objects.all()
    serializer_class = LinksSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsAuthenticated]
    filter_fields = ['user_name']
    search_fields = ['user_name', 'time_create']
    ordering_fields = ['user_name', 'time_create']
