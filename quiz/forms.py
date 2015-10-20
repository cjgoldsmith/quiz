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
