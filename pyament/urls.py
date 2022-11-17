from django.urls import path
from . import views

urlpatterns = [
    path('payment/', views.index, name="payment"),
    path('charge/', views.charge, name="charge"),
    path('success/<str:args>/', views.successMsg, name="success"),
]
