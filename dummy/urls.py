from django.urls import path, include
from rest_framework.routers import DefaultRouter

from dummy import views


app_name = 'dummy'
router = DefaultRouter()
router.register('tags', views.TagViewSet)

urlpatterns = [
    path('', include(router.urls))
]
