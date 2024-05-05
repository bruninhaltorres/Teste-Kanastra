from rest_framework import viewsets

from django.http import JsonResponse
from django.middleware.csrf import get_token

from app.models import Person
from app.serializer import PersonSerializer

from rest_framework.permissions import IsAuthenticated

def get_csrf_token(request):
    token = get_token(request)
    return JsonResponse({'csrf_token': token})

class PersonViewSet(viewsets.ModelViewSet):

    # permission_classes = [IsAuthenticated]

    queryset = Person.objects.all()
    serializer_class = PersonSerializer
