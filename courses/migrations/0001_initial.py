# Generated by Django 2.1.7 on 2019-02-12 03:55

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('position', models.IntegerField()),
                ('thumbnail_image', models.ImageField(upload_to='media/')),
                ('video_file_path', models.FileField(upload_to='media/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'mkv', 'mov', 'avi', 'flv', 'mpg', 'wmv'])])),
                ('slug', models.SlugField(unique=True)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_file_url', models.FileField(upload_to='media/')),
            ],
        ),
    ]
