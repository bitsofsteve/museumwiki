from rest_framework import generics

from .models import Wiki
from.serializers import WikiSerializer


class WikiList(generics.ListCreateAPIView):
    queryset = Wiki.objects.all()
    serializer_class = WikiSerializer

class WikiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wiki.objects.all()
    serializer_class = WikiSerializer

