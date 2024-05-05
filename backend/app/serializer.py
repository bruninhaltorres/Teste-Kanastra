"""Mapeamento dos modelos de banco de dados para representações serializadas, como JSON"""

from rest_framework import serializers
from app.models import Person

from app.validators import *

class CustomDateField(serializers.DateField):
    def __init__(self, *args, **kwargs):
        date_formats = ['%d/%m/%Y', '%Y-%m-%d']
        kwargs['input_formats'] = date_formats
        super().__init__(*args, **kwargs)

class PersonSerializer(serializers.ModelSerializer):

    debtDueDate = CustomDateField()

    class Meta:
        model = Person
        fields = ['id', 'name', 'governmentId', 'email', 'debtAmount', 'debtDueDate']

    """
    def validate(self, data):
        if not cpf_valido(data['governmentId']):
            raise serializers.ValidationError({'governmentId': "Número de CPF inválido"})
        if not nome_valido(data['name']):
            raise serializers.ValidationError({'name': "Não inclua números nesse campo"})

        return data
    """