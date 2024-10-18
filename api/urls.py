from django.urls import path

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import ContactLCAPIView, ContactRUDAPIView


schema_view = get_schema_view(
    openapi.Info(
        title="API для отслеживания заявок",
        default_version='v1',
        description="Документация к API для отслеживания заявок.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(
            name="Alltch", 
            url="https://t.me/alltchumb",
            email="alltchumb05@gmail.com"
        ),
        license=openapi.License(
            name="MIT License"
        ),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('contact/', ContactLCAPIView.as_view(), name='contact-list-create'),
    path('contactrud/<int:pk>/', ContactRUDAPIView.as_view(), name='contact-detail'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]