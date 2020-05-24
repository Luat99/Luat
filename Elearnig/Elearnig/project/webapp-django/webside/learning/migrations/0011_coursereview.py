# Generated by Django 2.2.7 on 2020-05-23 16:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('learning', '0010_course_instructor_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseReview',
            fields=[
                ('review_id', models.AutoField(primary_key=True, serialize=False)),
                ('review_star', models.CharField(max_length=127)),
                ('review_content', models.CharField(max_length=500)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning.Course')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
