from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Lesson
from .forms import MultipleQuestionsForm


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
        context['question_form'] = MultipleQuestionsForm(extra=questions)
        return context

