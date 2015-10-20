from django import forms
from .models import Question


class QuestionAdminForm(forms.ModelForm):

    bool_radio = forms

    class Meta:
        model = Question
        fields = '__all__'
        widgets = {
            'answer': forms.RadioSelect(choices=Question.answer_choices)
        }


class MultipleQuestionsForm(forms.Form):

    def __init__(self, *args, **kwargs):

        extra = kwargs.pop('extra')
        super(MultipleQuestionsForm, self).__init__(*args, **kwargs)
        for i, question in enumerate(extra):
            self.fields['custom_%s_%s' % (i, question.id)] = \
                forms.BooleanField(
                    label=question.question,
                    widget=forms.RadioSelect(choices=Question.answer_choices))
