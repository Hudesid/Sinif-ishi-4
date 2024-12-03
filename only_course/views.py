from rest_framework import viewsets
from . import serializers, models


class InstructorViewSet(viewsets.ModelViewSet):
    queryset = models.Instructor.objects.all()
    serializer_class = serializers.InstructorSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer


class LessonViewSet(viewsets.ModelViewSet):
    queryset = models.Lesson.objects.all()
    serializer_class = serializers.LessonSerializer

