from rest_framework import serializers 
from pets.models import Cat , Dog

class DogSerializer(serializers.ModelSerializer):
    class Meta :
        model = Dog
        fields = '__all__'

class CatSerializer(serializers.ModelSerializer):
    class Meta :
        model = Cat
        fields = '__all__'
        