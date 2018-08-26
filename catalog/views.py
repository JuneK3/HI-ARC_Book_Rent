from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers

class ListAllBooks(APIView):

    def get(self, request, format=None):
        all_books = models.Book.objects.all()
        serializer = serializers.BookSerializer(all_books, many=True)

        return Response(data=serializer.data)

