from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Wiki
from .serializers import WikiSerializer


class WikiList(APIView):
    def get(self, request, format=None):
        wiki = Wiki.objects.all()
        serializer = WikiSerializer(wiki, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WikiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WikiDetail(APIView):
    def get_object(self, pk):
        try:
            return Wiki.objects.get(pk=pk)
        except Wiki.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        wiki = self.get_object(pk)
        serializer = WikiSerializer(wiki)
        return Response(serializer.data)
