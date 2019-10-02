from rest_framework import serializers
from .models import RecortesRecorte


class RecortesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecortesRecorte
        # fields = '__all__'
        fields = ('numeracao_unica',)
