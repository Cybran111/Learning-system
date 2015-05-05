from django.contrib import admin

from courses.assessments.models import QuestionSet, Question, PossibleAnswer, StudentAnswer, StudentAnswerSet
# Register your models here.

admin.site.register((QuestionSet, Question, PossibleAnswer, StudentAnswerSet, StudentAnswer))