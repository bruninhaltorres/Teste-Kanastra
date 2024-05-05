from django.contrib import admin
from django.urls import path, include

from app.views import *
from rest_framework import routers

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API Recursos",
        default_version='v1',
        description="Gerenciamento de Recursos",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Rotas principais:
router = routers.DefaultRouter()
router.register('charges', PersonViewSet, basename='Persons')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('get-csrf-token/', get_csrf_token, name='get_csrf_token'),

    # Rota para endpoint sem barra
    path('charges', PersonViewSet.as_view({'get': 'list', 'post': 'create', 'delete': 'delete'}), name='charges_no_slash'),

    path('', include(router.urls))
] 