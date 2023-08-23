from django.urls import path
from .views import home_view, introduce_view, form_view, quiz_view, result_view

app_name = 'quiz'

urlpatterns = [
    path('', home_view, name = 'home'),
    path('introduce_view', introduce_view, name = 'introduce'),
    path('form/', form_view, name = 'form'),
    path('quiz/<int:id>/', quiz_view, name = 'quiz'),
    path('result/', result_view, name = 'result'),
]