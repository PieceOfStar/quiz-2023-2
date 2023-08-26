from django.urls import path
from .views import home_view, form_view, easy_quiz_view, normal_quiz_view, hard_quiz_view, result_view

app_name = 'quiz'

urlpatterns = [
    path('', home_view, name = 'home'),
    path('form/', form_view, name = 'form'),
    path('quiz/easy/<int:num>/<str:user_answer>/', easy_quiz_view, name = 'easy'),
    path('quiz/normal/<int:num>/<str:user_answer>/', normal_quiz_view, name = 'normal'),
    path('quiz/hard/<int:num>/', hard_quiz_view, name = 'hard'),
    path('result/', result_view, name = 'result'),
]