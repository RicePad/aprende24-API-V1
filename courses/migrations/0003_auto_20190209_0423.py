# Generated by Django 2.1.5 on 2019-02-09 04:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_remove_lesson_video_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='video_file',
            new_name='video_file_path',
        ),
    ]
