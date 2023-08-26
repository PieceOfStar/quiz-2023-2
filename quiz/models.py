from django.db import models

SIMPLE_CATEGORY = (
    ('객관식', '객관식'),
    ('OX', 'OX'),
    ('주관식', '주관식'),
)

ANSWER_CHOICES = (
    ('선택지1', '선택지1'),
    ('선택지2', '선택지2'),
    ('선택지3', '선택지3'),
)
class Participant(models.Model):
    name = models.CharField(verbose_name = '이름', max_length = 10, null = False)
    student_id = models.CharField(verbose_name = '학번', max_length = 10, null = False)
    phone_num = models.CharField(verbose_name = '전화번호', max_length = 13, null = False)
    score = models.IntegerField(verbose_name = '점수')
    
class QuizSimple(models.Model):
    quiz_num = models.IntegerField(verbose_name = '퀴즈 번호')
    category = models.CharField(verbose_name = '카테고리', max_length = 10, choices = SIMPLE_CATEGORY, default = '객관식')
    question = models.CharField(verbose_name = '퀴즈', max_length = 250)
    answer_choices = models.CharField(verbose_name = '선택지', max_length = 100, choices = ANSWER_CHOICES, default = 'nothing')
    is_showed = models.BooleanField(verbose_name = '사용자에게 보여줬는지', default = False)
    sum_score = models.IntegerField(verbose_name = '사용자 누적 점수', default = 0)
    
class QuizInput(models.Model):
    quiz_num = models.IntegerField(verbose_name = '퀴즈 번호')
    category = models.CharField(verbose_name = '카테고리', max_length = 10, choices = SIMPLE_CATEGORY, default = '주관식')
    answer = models.CharField(verbose_name = '정답', max_length = 10)
    is_showed = models.BooleanField(verbose_name = '사용자에게 보여줬는지', default = False)
    sum_score = models.IntegerField(verbose_name = '사용자 누적 점수', default = 0)