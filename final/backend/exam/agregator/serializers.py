from agregator.models import Results
from rest_framework import serializers


class ResultsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Results
        fields = ('rank', 'direct_link')


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Results
        fields = ('rank', 'direct_link', 'source_link', 'site', 'date')
