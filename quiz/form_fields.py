from django import forms
from django.core.exceptions import ObjectDoesNotExist

from .models import Lesson

import json


class LessonObjectField(forms.IntegerField):
    """
    Allows us to check for a lesson pk field
    and retrieve that object if available. Otherwise
    raise a validation error.
    """
    def to_python(self, value):

        value = super(LessonObjectField, self).to_python(value)
        try:
            value = Lesson.objects.get(pk=value)
            return value
        except ObjectDoesNotExist:
            raise forms.ValidationError('Unable to locate this lesson.')


class JsonField(forms.CharField):
    """
    Allows us to load a json encoded field as a native python object.
    """
    def to_python(self, value):

        value = super(JsonField, self).to_python(value)
        try:
            value = json.loads(value)
            return value
        except ValueError as e:
            raise forms.ValidationError('Json encoded field contains non json')
