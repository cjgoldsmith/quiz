# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InstructionalContent',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('instruction', models.TextField(help_text='Text block containing instructional learning material')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('number_of_questions', models.IntegerField(help_text='Number of questions to pull into a quiz.', default=10)),
                ('passing_percentage', models.IntegerField(help_text='Percentage value (0 - 100) that qualifies as a passed lesson.', default=60)),
                ('instructions', models.ManyToManyField(to='quiz.InstructionalContent')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('question', models.CharField(max_length=255)),
                ('answer', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='lesson',
            name='questions',
            field=models.ManyToManyField(to='quiz.Question'),
        ),
    ]
