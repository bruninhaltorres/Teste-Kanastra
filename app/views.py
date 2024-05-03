from rest_framework import viewsets

from app.models import Person
from app.serializer import PersonSerializer

from rest_framework.permissions import IsAuthenticated

class PersonViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]

    queryset = Person.objects.all()
    serializer_class = PersonSerializer
