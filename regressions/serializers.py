from rest_framework import serializers
from regressions.models import Run, Test

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('label','status','duration','created','updated','start','end','run')

class RunSerializer(serializers.ModelSerializer):
    class Meta:
        model = Run
        fields = ('id','label','status','duration','submitter','created','updated','start','end','test_set','successes','failures','total_tests_run')