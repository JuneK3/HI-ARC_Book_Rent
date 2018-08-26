from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers

class ListAllBooks(APIView):

    def get(self, request, format=None):
        all_books = models.Book.objects.all()
        serializer = serializers.BookSerializer(all_books, many=True)

        return Response(data=serializer.data)

class ListAllAuthors(APIView):

    def get(self, request, format=None):
        all_authors = models.Author.objects.all()
        serializer = serializers.AuthorSerializer(all_authors, many=True)

        return Response(data=serializer.data)

class ListAllGenres(APIView):

    def get(self, request, format=None):
        all_genre = models.Genre.objects.all()
        serializer = serializers.GenreSerializer(all_genre, many=True)

        return Response(data=serializer.data)

class ListAllLanguages(APIView):

    def get(self, request, format=None):
        all_language = models.Language.objects.all()
        serializer = serializers.LanguageSerializer(all_language, many=True)

        return Response(data=serializer.data)

class ListAllBookInstances(APIView):

    def get(self, request, format=None):
        all_instances = models.BookInstance.objects.all()
        serializer = serializers.BookInstanceSerializer(all_instances, many=True)

        return Response(data=serializer.data)


