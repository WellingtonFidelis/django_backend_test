from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import FormTestViewSet

router = routers.DefaultRouter()
router.register('form_test', FormTestViewSet)

urlpatterns = [
        path('', include(router.urls)),
        ]
