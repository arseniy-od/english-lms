# Generated by Django 4.1.5 on 2023-02-17 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_rename_test_quiz_rename_testvar_quizvar'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='type',
            field=models.CharField(choices=[('MultipleChoice', 'Multiple Choice'), ('ExactMatch', 'Exact Match'), ('Var', 'Variants')], default='Var', max_length=100),
        ),
    ]
