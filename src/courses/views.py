from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, View
from .models import Course, Theme, Task, Test
from django.core.paginator import Paginator

from .forms import create_test_form


def index(request):
    if request.user.is_authenticated:
        courses = Course.objects.filter(student=request.user)
        return render(request, 'courses/index.html', {'courses': courses})
    else:
        return render(request, 'courses/index.html')


class CourseDetail(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'


class ThemeDetail(DetailView):
    model = Theme
    template_name = 'courses/theme_detail.html'


class TaskDetail(View):
    def post(self, request, course_id, theme_id, task_id):
        response = check_test_results(request, task_id)
        return response

    def get(self, request, course_id, theme_id, task_id):
        course = Course.objects.get(id=course_id)
        theme = Theme.objects.get(id=theme_id)
        task = Task.objects.get(id=task_id)
        lectures = task.lecture_set.all()
        tests = task.test_set.all()
        if lectures:
            paginator = Paginator(lectures, 1)
            lecture_num = request.GET.get('lecture', 1)
            is_test = request.GET.get('test', 0)
            lecture_page = paginator.get_page(lecture_num)
            return render(request, 'courses/task_detail.html', {'task': task,
                                                                'course': course,
                                                                'theme': theme,
                                                                'lecture_page': lecture_page,
                                                                'lectures': lectures,
                                                                'tests': tests,
                                                                'is_test': is_test,
                                                                'is_paginated': True})
        return render(request, 'courses/task_detail.html', {'task': task, 'tests': tests, 'is_paginated': False})


def check_test_results(request, task_id):
    task = Task.objects.get(id=task_id)
    tests = task.test_set.all()
    results = []
    for test in tests:
        test_var = test.testvar_set.get(id=request.POST.get(str(test.id)))
        if test_var.is_correct:
            results.append('Correct')
        else:
            results.append('Incorrect')
    return render(request, 'courses/test_result.html', {'results': results})


def test(request):
    form = create_test_form()

    if request.method == 'POST':
        form = create_test_form()
        return render(request, 'courses/test.html', {'form': form})
    else:
        form = create_test_form()
        return render(request, 'courses/test.html', {'form': form})


    # return render(request, 'courses/test.html', {'form': form})