from rest_framework import serializers
from .models import task , owner

class taskserializer(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = "__all__"

class ownerserializer(serializers.ModelSerializer):
    class Meta:
        model = owner
        fields = "__all__"