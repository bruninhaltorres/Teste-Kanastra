from rest_framework import serializers
from app.models import Person

from app.validators import *

class CustomDateField(serializers.DateField):
    def __init__(self, *args, **kwargs):
        kwargs['input_formats'] = ['%d/%m/%Y']  # Formato DD-MM-YYYY
        super().__init__(*args, **kwargs)

class PersonSerializer(serializers.ModelSerializer):

    debtDueDate = CustomDateField()

    class Meta:
        model = Person
        fields = ['name', 'governmentId', 'email', 'debtAmount', 'debtDueDate']

    def validate(self, data):
        if not cpf_valido(data['governmentId']):
            raise serializers.ValidationError({'governmentId': "Número de CPF inválido"})
        if not nome_valido(data['name']):
            raise serializers.ValidationError({'name': "Não inclua números nesse campo"})

        return data