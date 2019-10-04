from django.urls import path, include
from .views import RecortesAPIView


urlpatterns = [
    path('', include('api_recortes.user.urls')),
    path('recortes/', RecortesAPIView.as_view(), name='recortes'),
]
