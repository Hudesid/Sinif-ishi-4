from rest_framework import serializers
from .models import Instructor, Course, Lesson


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ('name', 'email', 'specialty')

    def validate_email(self, value):
        if Instructor.objects.filter(email=value).exists():
            raise serializers.ValidationError({"email": 'Bu email manzil allaqachon mavjud.'})
        return value


class CourseSerializer(serializers.ModelSerializer):
    teacher = InstructorSerializer(read_only=True)

    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'start_at', 'end_at', 'teacher')

    def validate(self, data):
        start_at = data.get('start_at')
        end_at = data.get('end_at')

        if start_at and end_at and start_at > end_at:
            raise serializers.ValidationError({
                'non_field_errors': "Kursning boshlanish sanasi tugash sanasidan oldin bo'lishi kerak.",
            })

        return data

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['course'] = CourseSerializer(instance.course).data
        return representation


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ('id', 'title', 'description', 'course', 'order')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['course'] = CourseSerializer(instance.course).data
        return representation

    def validate_order(self, value):
        if value < 0:
            raise serializers.ValidationError({"order": "Tartib raqami musbat butun son bo'lishi kerak."})
        return value
