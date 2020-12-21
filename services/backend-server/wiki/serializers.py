from rest_framework import serializers
from .models import Wiki


class WikiSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wiki
        fields = '__all__'
        read_only_fields = ('id', 'created_date', 'updated_date')