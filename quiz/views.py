from django.shortcuts import render, redirect
from .forms import ParticipantForm

def home_view(request):
    return render(request, 'quiz/home.html')

def form_view(request):
    
    if request.method == 'GET':
        form = ParticipantForm()
        context = { 'form' : form, }
        return render(request, 'quiz/form.html', context)
        
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quiz:home')  # 회원가입 성공 시 이동할 페이지
    
    return render(request, 'participant_signup.html', {'form': form})
    return render(request, 'quiz/form.html')

def quiz_view(request):
    return render(request, 'quiz/quiz.html')

def result_view(request):
    return render(request, 'quiz/result.html')