from django.contrib import admin
from .models import InstructionalContent
from .models import Question
from .models import Lesson
from .forms import QuestionAdminForm


class QuestionAdmin(admin.ModelAdmin):
    form = QuestionAdminForm

admin.site.register(InstructionalContent)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Lesson)
