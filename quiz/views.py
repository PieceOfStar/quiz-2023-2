from django.shortcuts import render, redirect

from quiz.forms import ParticipantForm
from .models import QuizEasy, QuizNormal, QuizHard, Participant

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
            participant = form.save()
            
            # 참가자의 학번을 쿠키에 저장
            response = redirect('quiz:normal', num = 1, user_answer = 'start')
            response.set_cookie('participant_student_id', participant.student_id)
            return response
    
    return render(request, 'quiz/form.html') # 등록에 실패한다면 다시 폼 보여주기

def easy_quiz_view(request, num, user_answer):
    
    next_num = num + 1 # 다음 페이지 전달을 위한 변수
    participant = get_participant(request = request) # 쿠키를 이용해서 참가자 정보 받아오기
    
    # 7 혹은 8이면 quiz-easy.html
    if (num == 7 or num == 8): 
        
        item = QuizEasy.objects.get(quiz_num = num) # 퀴즈 가져오기
        
        # num이 8 이면
        if(num == 8):
            previous_item = QuizEasy.objects.get(quiz_num = num-1) # 전 퀴즈 가져오기
            
            # 사용자의 정답과 퀴즈 정답이 일치한다면 
            if(user_answer == str(previous_item.answer)):
                participant.score += item.plus_score # 참가자의 점수 올리기
                participant.save() # 저장
                print('7번 정답, 점수 올림')
                
        context = { 
            'item' : item,
            'next_num' : next_num, 
        }
        print(participant.score)
        return render(request, 'quiz/quiz-easy.html', context)
    
    else:
        previous_item = QuizEasy.objects.get(quiz_num = num-1) # 전 퀴즈 가져오기
            
        # 사용자의 정답과 퀴즈 정답이 일치한다면 
        if(user_answer == str(previous_item.answer)):
            participant.score += 5 # 참가자의 점수 올리기
            participant.save() # 저장
            print('8번 정답, 점수 올림')
        
        print(participant.score)
        return redirect('quiz:hard', num = 9)

def normal_quiz_view(request, num, user_answer):
    
    next_num = num + 1 # 다음 페이지 전달을 위한 변수
    participant = get_participant(request = request) # 쿠키를 이용해서 참가자 정보 받아오기
    
    # 1~6이면 quiz-normal.html
    if (num >= 1 and num <= 6): 
        
        item = QuizNormal.objects.get(quiz_num = num) # 퀴즈 가져오기
    
        # num이 2 이상이면
        if(num >= 2):
            previous_item = QuizNormal.objects.get(quiz_num = num-1) # 전 퀴즈 가져오기
            
            # 사용자의 정답과 퀴즈 정답이 일치한다면 
            if(user_answer == str(previous_item.answer)):
                participant.score += item.plus_score # 참가자의 점수 올리기
                participant.save() # 저장
        
        # 전달
        context = { 
            'item' : item,
            'next_num' : next_num,
        }
        
        print(participant.score)
        
        return render(request, 'quiz/quiz-normal.html', context)
    
    else:
        previous_item = QuizNormal.objects.get(quiz_num = num-1) # 전 퀴즈 가져오기
            
        # 사용자의 정답과 퀴즈 정답이 일치한다면 
        if(user_answer == str(previous_item.answer)):
            participant.score += 10 # 참가자의 점수 올리기
            participant.save() # 저장
        
        print(participant.score)
        return redirect('quiz:easy', num = 7, user_answer = 'start')
    
def hard_quiz_view(request, num):
    
    item = QuizHard.objects.get(quiz_num = num) # 퀴즈 가져오기
    participant = get_participant(request = request) # 쿠키를 이용해서 참가자 정보 받아오기
    
    if request.method == 'POST':
        
        user_answer = request.POST.get('user_answer', None)
        if user_answer is not None:
            
            if num == 9:
                answer_dict = { 'answer9_1': item.answer9_1, 'answer9_2': item.answer9_2, 'answer9_3': item.answer9_3, }
                
                # for문을 돌며 user_answer와 비교
                for answer_key, correct_answer in answer_dict.items():
                    if user_answer == correct_answer: # 정답이면
                        participant.score += item.plus_score # 참가자의 점수 올리기
                        participant.save() # 저장
                
                # form 보여주기
                context = {
                    'item' : item,
                    'num' : 10,
                }
                
                print(participant.score)
                return render(request, 'quiz/quiz-hard.html', context)
            
            else:
                answer_dict = { 'answer10_1': item.answer10_1, 'answer10_2': item.answer10_2, 'answer10_3': item.answer10_3, }
                # for문을 돌며 user_answer와 비교
                for answer_key, correct_answer in answer_dict.items():
                    if user_answer == correct_answer: # 정답이면
                        participant.score += item.plus_score # 참가자의 점수 올리기
                        participant.save() # 저장

                # form 보여주기
                context = {
                    'item' : item,
                    'num' : num,
                }
                
                print(participant.score)
                return render(request, 'quiz/result.html', context)

    context = {
                    'item' : item,
                    'num' : num,
                }
    return render(request, 'quiz/quiz-hard.html', context)

def result_view(request):
    return render(request, 'quiz/result.html')

# 참가자 정보 가져오기
def get_participant(request):
    
    participant_student_id = request.COOKIES.get('participant_student_id')

    try:
        return Participant.objects.get(student_id=participant_student_id)
        
    except Participant.DoesNotExist:
        print("참가자 정보를 찾을 수 없습니다.")