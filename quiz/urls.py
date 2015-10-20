from django.conf.urls import patterns
from django.conf.urls import url

from .views import LessonListView
from .views import LessonView
from .views import QuizView

urlpatterns = patterns('',
                       url(r'^lesson/(?P<pk>\d+)/$', LessonView.as_view(), name='lesson-view'),
                       url(r'^quiz/(?P<pk>\d+)/$', QuizView.as_view(), name='quiz-view'),
                       url(r'^$', LessonListView.as_view(), name='lesson-list'), )
