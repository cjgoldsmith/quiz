from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.template.context_processors import csrf

from .models import Lesson
from .models import Question
from .forms import MultipleQuestionsForm
from .form_fields import JsonField

import json


class LessonListView(ListView):
    template_name = 'quiz/lessons/list.html'
    model = Lesson


class LessonView(DetailView):
    template_name = 'quiz/lessons/detail.html'
    model = Lesson


class QuizView(DetailView):
    template_name = 'quiz/lessons/quiz.html'
    model = Lesson

    def get_context_data(self, **kwargs):
        context = super(QuizView, self).get_context_data(**kwargs)
        lesson = context['object']
        questions = lesson.questions.all().order_by('?')[:lesson.number_of_questions]
        question_load = json.dumps([q.id for q in questions])

        context['question_form'] = MultipleQuestionsForm(
            initial={'lesson': lesson.id,
                     'question_load': question_load},
            extra=questions)

        context.update(csrf(self.request))
        return context


class QuizGradeView(FormView):
    form_class = MultipleQuestionsForm
    template_name = 'quiz/lessons/grade.html'

    def get_form_kwargs(self):
        kwargs = super(QuizGradeView, self).get_form_kwargs()
        questions = JsonField(required=True).clean(self.request.POST.get('question_load'))
        extra = []
        for q in questions:
            extra.append(Question.objects.get(pk=q))
        kwargs['extra'] = extra
        return kwargs

    def form_valid(self, form):

        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):

        form = kwargs.pop('form')
        context = super(QuizGradeView, self).get_context_data(**kwargs)

        # normally these private vars would be saved some other way, this is
        # a hack for speed.
        passed = form._percent >= form.cleaned_data['lesson'].passing_percentage
        context['score'] = form._right
        context['percent'] = form._percent
        context['passed'] = passed
        return context
