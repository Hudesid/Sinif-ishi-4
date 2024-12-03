# from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'instructor', views.InstructorViewSet)
router.register(r'course', views.CourseViewSet)
router.register(r'lesson', views.LessonViewSet)

urlpatterns = router.urls