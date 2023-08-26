from django.shortcuts import render, redirect
from .forms import ParticipantForm
from .models import QuizEasy, QuizNormal, QuizHard

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
            return redirect('quiz:normal', num = 1, user_answer = None)
    
    return render(request, 'quiz/form.html') # 등록에 실패한다면 다시 폼 보여주기

def easy_quiz_view(request, num):
    
    next_num = num + 1
    
    if (num == 7 or num <= 8): # 7 혹은 8이면 quiz-easy.html
        
        item = QuizEasy.objects.get(quiz_num = num)
        context = { 
            'item' : item,
            'next_num' : next_num, 
        }
        return render(request, 'quiz/quiz-easy.html', context)
    
    else:
        return redirect('quiz:hard', num = 9)

def normal_quiz_view(request, num, user_answer = None):
    
    print(user_answer)
    print(request)
    next_num = num + 1
    
    if (num >= 1 and num <= 6): # 1~6이면 quiz-normal.html
        
        item = QuizNormal.objects.get(quiz_num = num)
        
        if(num >= 2):
            previous_item = QuizNormal.objects.get(quiz_num = num-1)
            print(previous_item.answer)
            if(user_answer == str(previous_item.answer)):
                print("정답")
                item.sum_score += 10
        
        context = { 
            'item' : item,
            'next_num' : next_num,
        }
        return render(request, 'quiz/quiz-normal.html', context)
    
    else:
        return redirect('quiz:easy', num = 7)
    

def hard_quiz_view(request, num):
    # form 보여주기
    pass

def result_view(request):
    return render(request, 'quiz/result.html')