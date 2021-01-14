from rest_framework import serializers

from .models import MyFiles

class MyFileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyFiles
        fields = "__all__"