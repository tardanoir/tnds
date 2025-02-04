"""URL configuration for {{ cookiecutter.project_name }} project."""

from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import MLModelViewSet

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r"models", MLModelViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),
]
