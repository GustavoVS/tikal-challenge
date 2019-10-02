from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView
from .serializers import RecortesSerializer


class RecortesAPIView(RetrieveAPIView):
    serializer_class = RecortesSerializer

    def get_object(self):
        pass
