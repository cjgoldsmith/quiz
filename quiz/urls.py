from django.conf.urls import patterns
from django.conf.urls import url

from .views import LessonListView
from .views import LessonView

urlpatterns = patterns('',
                       url(r'^lesson/(?P<pk>\d+)/$', LessonView.as_view(), name='lesson-view'),
                       url(r'^$', LessonListView.as_view(), name='lesson-list'), )
