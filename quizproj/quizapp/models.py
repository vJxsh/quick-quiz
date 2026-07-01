from django.db import models
from django.utils import timezone
import random
import string

import datetime

# Create your models here.

def quiz_code_generator():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

class QuizInstance(models.Model):
    creator_name = models.CharField(max_length=64)
    code = models.CharField(max_length=8, default=quiz_code_generator, unique=True)
    quiz_title = models.CharField(max_length=64, default=code)
    pub_date = models.DateTimeField(auto_now_add=True)
    latest_updated_date = models.DateTimeField('date when latest updated', auto_now=True)
    
class Question(models.Model):
    quiz_instance = models.ForeignKey(QuizInstance, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=256)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    latest_updated_date = models.DateTimeField('date when latest updated', auto_now=True)
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=256)
    
    
    
