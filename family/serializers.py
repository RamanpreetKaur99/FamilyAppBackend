from rest_framework import serializers 
from .models import Groceries, ToDo, Event, Bills

class GroceriesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Groceries
        fields='__all__'

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class BillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bills
        fields = '__all__'