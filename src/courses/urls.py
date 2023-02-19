from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('course/<int:pk>', CourseDetail.as_view(), name='course_detail'),
    path('course/<int:course_id>/theme/<int:pk>', ThemeDetail.as_view(), name='theme_detail'),
    path('course/<int:course_id>/theme/<int:theme_id>/task/<int:task_id>', TaskDetail.as_view(), name='task_detail'),
]
