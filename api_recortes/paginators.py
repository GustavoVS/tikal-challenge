from rest_framework.pagination import LimitOffsetPagination


class RecortesPaginator(LimitOffsetPagination):
    limit_query_param = 'size'
    default_limit = 50
