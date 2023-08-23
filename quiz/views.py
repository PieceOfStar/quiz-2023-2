from django.shortcuts import render

def home_view(request):
    return render(request, 'quiz/home.html')

def introduce_view(request):
    return render(request, 'quiz/introduce.html')

def form_view(request):
    return render(request, 'quiz/form.html')

def quiz_view(request):
    return render(request, 'quiz/quiz.html')

def result_view(request):
    return render(request, 'quiz/result.html')