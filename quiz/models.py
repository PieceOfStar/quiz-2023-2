from django.db import models

CATEGORY = (
    ('easy', 'easy'),
    ('normal', 'normal'),
    ('hard', 'hard'),
)
    
class Participant(models.Model):
    name = models.CharField(verbose_name = '이름', max_length = 10, null = False)
    student_id = models.CharField(verbose_name = '학번', max_length = 10, null = False)
    phone_num = models.CharField(verbose_name = '전화번호', max_length = 13, null = False)
    score = models.IntegerField(verbose_name = '점수', default = 0)
    
class QuizEasy(models.Model):
    quiz_num = models.IntegerField(verbose_name = '퀴즈 번호')
    category = models.CharField(verbose_name = '카테고리', max_length = 10, choices = CATEGORY, default = 'easy')
    question = models.CharField(verbose_name = '내용', max_length = 250)
    choices1 = models.CharField(verbose_name = '선택지1', max_length = 100, default = 'O')
    choices2 = models.CharField(verbose_name = '선택지2', max_length = 100, default = 'X')
    answer = models.CharField(verbose_name = '정답', max_length = 100)
    plus_score = models.IntegerField(verbose_name = '플러스 점수', default = 5)
    
class QuizNormal(models.Model):
    quiz_num = models.IntegerField(verbose_name = '퀴즈 번호')
    category = models.CharField(verbose_name = '카테고리', max_length = 10, choices = CATEGORY, default = 'normal')
    question = models.CharField(verbose_name = '내용', max_length = 250)
    choices1 = models.CharField(verbose_name = '선택지1', max_length = 100)
    choices2 = models.CharField(verbose_name = '선택지2', max_length = 100)
    choices3 = models.CharField(verbose_name = '선택지3', max_length = 100)
    answer = models.CharField(verbose_name = '정답', max_length = 100)
    plus_score = models.IntegerField(verbose_name = '플러스 점수', default = 10)
    
class QuizHard(models.Model):
    quiz_num = models.IntegerField(verbose_name = '퀴즈 번호')
    category = models.CharField(verbose_name = '카테고리', max_length = 10, choices = CATEGORY, default = 'hard')
    question = models.CharField(verbose_name = '내용', max_length = 250)
    answer9_1 = models.CharField(verbose_name = '9변_1 정답', max_length = 10, default = '빅뱅')
    answer9_2 = models.CharField(verbose_name = '9번_2 정답', max_length = 10, default = '빅뱅이론')
    answer9_3 = models.CharField(verbose_name = '9번_3 정답', max_length = 10, default = '빅뱅 이론')
    answer10_1 = models.CharField(verbose_name = '10번_1 정답', max_length = 10, default = '405')
    answer10_2 = models.CharField(verbose_name = '10번_2 정답', max_length = 10, default = '405호')
    answer10_3 = models.CharField(verbose_name = '10번_3 정답', max_length = 10, default = '인성관 405호')
    plus_score = models.IntegerField(verbose_name = '플러스 점수', default = 15)