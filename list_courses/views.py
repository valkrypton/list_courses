from rest_framework import generics

from list_courses.filters import build_course_filters
from list_courses.serializers import CourseOverviewSerializer

from openedx_catalog.models import CourseRun



class CourseListAPIView(generics.ListAPIView):
    """
    GET /api/list_courses/courses/

    Lists courses, optionally filtered by ``title`` (case-insensitive
    partial match) and/or ``language`` (exact match) query parameters.
    The two filters can be combined.
    """
    serializer_class = CourseOverviewSerializer

    def get_queryset(self):
        title = self.request.query_params.get('title')
        language = self.request.query_params.get('language')
        return CourseRun.objects.filter(build_course_filters(title, language))
