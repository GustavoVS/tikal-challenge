from datetime import datetime
from django.http import Http404
from django.db.models import Q
from functools import reduce
import re
import operator
from rest_framework.exceptions import ParseError
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import RecortesSerializer
from .models import RecortesRecorte
from .paginators import RecortesPaginator


class RecortesAPIView(ListAPIView):
    serializer_class = RecortesSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = RecortesPaginator

    def get_queryset(self):

        nup = self.request.query_params.get('nup')
        q = self.request.query_params.get('q')
        t = self.request.query_params.get('t')

        # if not(nup or q or t):
        #     raise ParseError('Missing required parameters')

        if t:
            try:
                t = datetime.strptime(t, '%d%m%Y')
            except ValueError:
                raise ParseError("Incorrect date format in \"t\", should be ddmmyyyy")

        qs = RecortesRecorte.objects.all().order_by('id')

        if nup:
            qs = qs.filter(numeracao_unica=nup)

        if q:
            qs = qs.filter(reduce(operator.and_, (Q(recorte__contains=rec)
                           for rec in q.split('-'))))

        if t:
            qs = qs.filter(data_publicacao=t)

        if not qs:
            raise Http404()

        # size = self.request.query_params.get('size')
        # offset = self.request.query_params.get('offset')

        # if offset:
        #     offset = int(re.sub("\D", "", offset) or 0)

        # if size:
        #     size = int(re.sub("\D", "", size) or 0)
        #     if offset:
        #         size += offset

        # return qs[offset:size]
        return qs
