from rest_framework.serializers import ModelSerializer

from links.models import Links


class LinksSerializer(ModelSerializer):
    class Meta:
        model = Links
        fields = '__all__'
