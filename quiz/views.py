from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Lesson


class LessonListView(ListView):
    template_name = 'quiz/lessons/list.html'
    model = Lesson


class LessonView(DetailView):
    template_name = 'quiz/lessons/detail.html'
    model = Lesson

