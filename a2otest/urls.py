from django.urls import path
from . import views

urlpatterns = [
    path('problema-1/<t>/', views.Problema1.as_view(), name='problema-1'),
    path('problema-2', views.Problema2.as_view(), name='problema-2'),
]
