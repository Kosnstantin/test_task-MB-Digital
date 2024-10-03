from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeamViewSet, PersonViewSet

router = DefaultRouter() # router instance

# endpoints for CRUD
router.register('teams', TeamViewSet)
router.register('people', PersonViewSet)

# route list
urlpatterns = [
    path('', include(router.urls)),
]
