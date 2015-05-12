from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class QuestionSet(models.Model):
    POSSIBLE_TYPES = (
        ("multiset", "Multiple checkboxes"), ("singleset", "Radiobuttons"),
        ("multiset_custom", "Multiple checkboxes with student's own answer"),
        ("singleset_custom", "Radiobuttons with student's own answer")
    )

    type = models.TextField(choices=POSSIBLE_TYPES)
    title = models.TextField(unique=True)
    # Some description directly in assessment
    description = models.TextField()
    number = models.IntegerField()
    max_questions = models.PositiveIntegerField()
    course = models.ForeignKey("courses.Course")
    week = models.ForeignKey("courses.Week")

    class Meta:
        unique_together = ('number', 'course', 'week', 'title')
        ordering = ('number',)


class Question(models.Model):
    questionset = models.ForeignKey(QuestionSet)
    number = models.IntegerField()
    text = models.TextField()
    explanation = models.TextField(blank=True, default="")
    value = models.PositiveIntegerField()

    class Meta:
        unique_together = (
            ('questionset', 'number'),
            ('questionset',  'text')
        )


class PossibleAnswer(models.Model):
    text = models.TextField()
    correct_value = models.TextField(blank=True, default="")
    is_correct = models.BooleanField(default=False)
    explanation = models.TextField(blank=True, default="")
    question = models.ForeignKey(Question)
    number = models.IntegerField()

    class Meta:
        unique_together = (
            ('question', 'number'),
            ('question', 'text')
        )

        ordering = ('number',)


class StudentAnswerSet(models.Model):
    user = models.ForeignKey(User)
    questionset = models.ForeignKey(QuestionSet)
    assigned_question = models.ManyToManyField(Question)
    mark = models.PositiveIntegerField(default=0)
    is_finished = models.BooleanField(default=False)
    number = models.IntegerField()

    class Meta:
        unique_together = ('user', 'number', "questionset")


class StudentAnswer(models.Model):
    answerset = models.ForeignKey(StudentAnswerSet)
    question = models.ForeignKey(Question)
    chosed_answer = models.ForeignKey(PossibleAnswer)

    class Meta:
        unique_together = ('answerset', 'question', 'chosed_answer')
