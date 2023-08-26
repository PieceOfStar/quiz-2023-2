from django.contrib import admin
from .models import Participant, QuizSimple, QuizInput

@admin.register(Participant)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'student_id', 'phone_num', 'score')
    pass

@admin.register(QuizSimple)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('quiz_num', 'category', 'question', 'answer_choices', 'is_showed', 'sum_score')
    pass

@admin.register(QuizInput)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('quiz_num', 'category', 'answer', 'is_showed', 'sum_score')
    pass