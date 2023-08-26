from django.urls import path
from .views import home_view, form_view, quiz_view, result_view

app_name = 'quiz'

urlpatterns = [
    path('', home_view, name = 'home'),
    path('form/', form_view, name = 'form'),
    path('quiz/<int:id>/', quiz_view, name = 'quiz'),
    path('result/', result_view, name = 'result'),
]