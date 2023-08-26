from django.contrib import admin
from .models import Participant, QuizEasy, QuizNormal, QuizHard

@admin.register(Participant)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'student_id', 'phone_num', 'score')
    pass

@admin.register(QuizEasy)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('quiz_num', 'question', 'answer')
    pass

@admin.register(QuizNormal)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('quiz_num', 'question', 'answer')
    pass

@admin.register(QuizHard)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('quiz_num', 'question')
    pass
