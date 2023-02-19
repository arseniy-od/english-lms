from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, View
from .models import Course, Theme, Task, Quiz
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
        task = Task.objects.get(id=task_id)
        lectures = task.lecture_set.all()
        quizes = task.quiz_set.all()
        quizes_multiple_choice = task.quizmultiplechoice_set.all()
        is_quiz_page = request.GET.get('quiz', 0)
        lecture_page = get_lecture_page(request, lectures)
        is_paginated = bool(lecture_page)
        return render(request, 'courses/task_detail.html', {'task': task,
                                                            'lecture_page': lecture_page,
                                                            'lectures': lectures,
                                                            'quizes': quizes,
                                                            'quizes_multiple_choice': quizes_multiple_choice,
                                                            'is_quiz_page': is_quiz_page,
                                                            'is_paginated': is_paginated})


def get_lecture_page(request, lectures):
    if lectures:
        paginator = Paginator(lectures, 1)
        lecture_num = request.GET.get('lecture', 1)
        lecture_page = paginator.get_page(lecture_num)
        return lecture_page
    else:
        return None


def check_test_results(request, task_id):
    task = Task.objects.get(id=task_id)
    quizes = task.test_set.all()
    quizes_multi = task.quizmultiplechoice_set.all()
    results = []
    if quizes:
        check_quiz_choice(quizes)
    if quizes_multi:
        check_quiz_choice(quizes_multi)
    return render(request, 'courses/test_result.html', {'results': results})


def check_quiz_choice(quizes):  # QuerySet
    for quiz in quizes:
        quizvar_id = request.POST.get(str(quiz.id))
        quiz_var = quiz.testvar_set.get(id=quizvar_id)
        if quiz_var.is_correct:
            results.append('Correct')
        else:
            results.append('Incorrect')