from django.urls import path
from .views import RecortesAPIView


urlpatterns = [
    path('recortes/', RecortesAPIView.as_view(), name='recortes')
]
