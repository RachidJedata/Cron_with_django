from django.urls import path
from . import views

urlpatterns = [
    path('crypto/', views.show_crypto_data, name='show_crypto_data'),
]