from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


class TotalPagesPagination(PageNumberPagination):

    page_size = 10

    def get_paginated_response(self, data):
        return Response({
            'total_pages': self.page.paginator.num_pages,
            'results': data,
        })
