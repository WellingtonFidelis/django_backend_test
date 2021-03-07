from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import FormTestViewSet
from . import views

router = routers.DefaultRouter()
router.register(r'form-test', FormTestViewSet,basename='form-test')

urlpatterns = [
        path('', include(router.urls)),
        ]
