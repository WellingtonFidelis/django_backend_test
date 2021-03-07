from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
# from .views import FormTestViewSet
from . import views

# router = routers.DefaultRouter()
# router.register(r'form-test', FormTestViewSet)

urlpatterns = [
#        path('', include(router.urls)),
        path('form-list', views.formList, name='form-list'),
        path('form-list-detail/<str:pk>/', views.formListDetail, name='form-list-detail' ),
        path('form-create', views.formCreate, name='form-create'),
        path('form-update/<str:pk>/', views.formUpdate, name='form-update'),
        path('form-delete/<str:pk>/', views.formDelete, name='form-delete'),
        ]
