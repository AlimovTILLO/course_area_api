# Generated by Django 4.0.6 on 2022-07-30 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_school_options_course_image_course_rating_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='course',
            name='title',
        ),
    ]