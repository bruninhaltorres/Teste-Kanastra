from django.contrib import admin
from django.urls import path, include

from app.views import PersonViewSet
from rest_framework import routers

# Rotas principais:
router = routers.DefaultRouter()
router.register('persons', PersonViewSet, basename='Persons')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', include(router.urls))
] 