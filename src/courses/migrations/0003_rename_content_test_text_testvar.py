# Generated by Django 4.1.5 on 2023-01-21 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_remove_test_is_correct'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test',
            old_name='content',
            new_name='text',
        ),
        migrations.CreateModel(
            name='TestVar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.test')),
            ],
        ),
    ]
