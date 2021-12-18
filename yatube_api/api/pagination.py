# api/pagination.py
from rest_framework.pagination import LimitOffsetPagination


class LimitOffsetPagination5(LimitOffsetPagination):
    page_size = 5
