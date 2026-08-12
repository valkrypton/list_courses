"""
URLs for list_courses.
"""
from django.urls import path

from list_courses.views import CourseListAPIView

urlpatterns = [
    path('courses/', CourseListAPIView.as_view(), name='course-list'),
]
