from rest_framework import serializers
from apps.contents.models import Contact, Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    auto = CarSerializer(read_only=True)
    class Meta:
        model = Contact
        fields = '__all__'

