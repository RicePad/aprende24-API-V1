# Generated by Django 2.1.5 on 2019-01-23 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='course_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='course_title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='lesson',
            old_name='lesson_title',
            new_name='title',
        ),
    ]
