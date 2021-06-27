from rest_framework import filters
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from apis.models import Contact, Address, InvoicePosition, Country, Invoice
from apis.serializers import ContactSerializer, AddressSerializer, InvoicePositionSerializer, CountrySerializer, \
    InvoiceSerializer


class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    filterset_fields = ['type']
    permission_classes = (IsAuthenticated,)


class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = (IsAuthenticated,)


class InvoicePositionViewSet(ModelViewSet):
    queryset = InvoicePosition.objects.all()
    serializer_class = InvoicePositionSerializer
    permission_classes = (IsAuthenticated,)


class CountryListView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['value']
    permission_classes = (IsAuthenticated,)


class InvoiceViewSet(ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['address__contact__name']
    permission_classes = (IsAuthenticated,)
