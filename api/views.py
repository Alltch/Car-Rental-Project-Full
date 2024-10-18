from django.shortcuts import render
from rest_framework import generics, permissions, pagination, status
from rest_framework.response import Response

from api.serializers import ContactSerializer

from apps.contents.models import Contact

class ContactLCAPIView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (permissions.IsAdminUser,)
    pagination_class = pagination.LimitOffsetPagination


class ContactRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (permissions.IsAdminUser,)
    lookup_field = 'pk'