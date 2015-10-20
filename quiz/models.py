from django.db import models


class InstructionalContent(models.Model):

    instruction = models.TextField(
        blank=False,
        help_text="Text block containing instructional learning material")

    def __str__(self):
        return type(self).__name__ + ": " + self.instruction[:50]


class Question(models.Model):

    answer_choices = ((True, 'Yes'), (False, 'No'))

    question = models.CharField(
        blank=False,
        max_length=255)

    answer = models.BooleanField(choices=answer_choices, default=True, null=False, blank=False)

    def __str__(self):
        return type(self).__name__ + ": " + self.question[:50]


class Lesson(models.Model):

    title = models.CharField(max_length=140)
    instructions = models.ManyToManyField(InstructionalContent)
    questions = models.ManyToManyField(Question)

    number_of_questions = models.IntegerField(
        default=10,
        help_text="Number of questions to pull into a quiz.")

    passing_percentage = models.IntegerField(
        default=60,
        help_text="Percentage value (0 - 100) that qualifies as a passed lesson.")

    def __str__(self):
        return type(self).__name__ + ": " + self.title[:50]
