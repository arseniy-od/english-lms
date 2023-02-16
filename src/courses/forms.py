from django import forms
from .models import Task, Test, TestVar, Lecture


# create a form for test
def create_test_form():
    tests = Test.objects.all()
    test_form = []
    for test in tests:
        test_var = test.testvar_set.all()
        test_form.append((test.id, test.content, test_var))
    return test_form


    # l = ((1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'))

    # class TestForm(forms.Form):
    #     choice = forms.ChoiceField(choices=l, widget=forms.RadioSelect)
    #
    # return TestForm