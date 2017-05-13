from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'programs', views.ProgramViewSet)
router.register(r'users', views.UserViewSet)

# Nested resources
program_router = routers.NestedSimpleRouter(router, r'programs', lookup='program')
program_router.register(r'days', views.DayViewSet, base_name='days')

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(program_router.urls)),
]
