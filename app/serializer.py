from rest_framework import serializers
from app.models import Person

class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ['name', 'governmentId', 'email', 'debtAmount', 'debtDueDate']