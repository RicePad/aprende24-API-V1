# Generated by Django 2.1.5 on 2019-01-22 02:54

from django.db import migrations, models
import video_dockerized.storange_backends


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0005_auto_20190118_0339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videotutorial',
            name='thumbnail_image',
            field=models.ImageField(storage=video_dockerized.storange_backends.PublicMediaStorage(), upload_to=''),
        ),
        migrations.AlterField(
            model_name='videotutorial',
            name='video_file',
            field=models.FileField(null=True, storage=video_dockerized.storange_backends.PublicMediaStorage(), upload_to='', verbose_name=''),
        ),
    ]
