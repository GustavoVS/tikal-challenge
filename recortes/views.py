from django.http import Http404
import re
from rest_framework.exceptions import ParseError
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import RecortesSerializer
from .models import RecortesRecorte


class RecortesAPIView(ListAPIView):
    serializer_class = RecortesSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):

        nup = self.request.query_params.get('nup')
        q = self.request.query_params.get('q')
        t = self.request.query_params.get('t')

        if not(nup or q or t):
            raise ParseError('Missing required parameters')

        qs = RecortesRecorte.objects.all()

        if nup:
            qs = qs.filter(numeracao_unica=nup)

        if not qs:
            raise Http404()

        size = self.request.query_params.get('size')
        offset = self.request.query_params.get('offset')

        if offset:
            offset = int(re.sub("\D", "", offset) or 0)

        if size:
            size = int(re.sub("\D", "", size) or 0)
            if offset:
                size += offset

        return qs[offset:size]
