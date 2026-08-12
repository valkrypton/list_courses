from rest_framework import serializers


class CourseOverviewSerializer(serializers.Serializer):
    course_id = serializers.CharField(source='id', read_only=True)
    title = serializers.CharField(source='display_name', read_only=True)
    language = serializers.CharField(read_only=True)
