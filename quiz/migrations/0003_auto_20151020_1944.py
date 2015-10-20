# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_lesson_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True),
        ),
    ]
