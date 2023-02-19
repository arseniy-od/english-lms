from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    student = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.title


class Theme(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Task(models.Model):
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


TYPE_CHOICES = (
    ('MultipleChoice', 'Multiple Choice'),
    ('ExactMatch', 'Exact Match'),
    ('Var', 'Variants'),
)


class Quiz(models.Model):
    type = models.CharField(max_length=100, choices=TYPE_CHOICES, default='Var')
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)

    def __str__(self):
        return self.content


class QuizMultipleChoice(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)

    def __str__(self):
        return self.content


class QuizExactMatch(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)

    def __str__(self):
        return self.content


class QuizVar(models.Model):
    test = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['content']


class QuizMultipleChoiceVar(models.Model):
    quiz = models.ForeignKey(QuizMultipleChoice, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['content']



class Lecture(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = RichTextUploadingField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
