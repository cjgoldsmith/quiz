from django import forms
from django.core.exceptions import ObjectDoesNotExist

from .models import Question
from .form_fields import LessonObjectField
from .form_fields import JsonField

import re


class QuestionAdminForm(forms.ModelForm):

    bool_radio = forms

    class Meta:
        model = Question
        fields = '__all__'
        widgets = {
            'answer': forms.RadioSelect(choices=Question.answer_choices)
        }


class MultipleQuestionsForm(forms.Form):

    lesson = LessonObjectField(
        required=True,
        widget=forms.HiddenInput)
    question_load = JsonField(
        required=True,
        widget=forms.HiddenInput)

    def __init__(self, *args, **kwargs):
        """
        Over riden to allow for dynamic form creation.
        """
        self._right = 0
        self._wrong = 0
        self._percent = 0.0

        extra = kwargs.pop('extra', [])
        super(MultipleQuestionsForm, self).__init__(*args, **kwargs)
        for i, question in enumerate(extra):
            self.fields['custom_%s_%s' % (i, question.id)] = \
                forms.BooleanField(
                    required=False,
                    label=question.question,
                    widget=forms.RadioSelect(choices=Question.answer_choices))

    def clean(self):
        """
        Clean method override allows us to perform a final validation check against
        all fields in a form together. In this case we are hijacking it to also extract
        extra fields added during init and calculate relevant scores and attach those values
        to the instance.
        """
        question_id_re = re.compile(r'\d+$')

        cleaned_data = super(MultipleQuestionsForm, self).clean()
        try:
            for k in self.cleaned_data:
                if str(k).startswith('custom_'):
                    m = re.search(question_id_re, str(k))
                    q = Question.objects.get(pk=int(m.group(0)))
                    if bool(cleaned_data[k]) == q.answer:
                        self._right += 1
                    else:
                        self._wrong += 1
        except ObjectDoesNotExist:
            raise forms.ValidationError('Unable to find Question.')

        self._percent = self._right/(self._right + self._wrong) * 100
        return cleaned_data
