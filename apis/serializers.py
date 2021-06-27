from rest_framework import serializers

from apis.models import Address, Contact, Country, InvoicePosition, Invoice


class AddressSerializer(serializers.ModelSerializer):
    country_name = serializers.CharField(source='country.value', read_only=True)
    contact_name = serializers.CharField(source='contact.name', read_only=True)

    class Meta:
        model = Address
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True, read_only=True)

    class Meta:
        model = Contact
        fields = '__all__'


class InvoicePositionSerializer(serializers.ModelSerializer):
    total = serializers.FloatField(read_only=True)

    class Meta:
        model = InvoicePosition
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class InvoiceSerializer(serializers.ModelSerializer):
    positions = InvoicePositionSerializer(many=True, read_only=True)
    total_amount = serializers.FloatField(read_only=True)

    class Meta:
        model = Invoice
        fields = '__all__'
