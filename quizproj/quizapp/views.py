from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.utils import timezone
from django.views import generic

from .forms import QuestionForm

from .models import QuizInstance, Question, Choice

import datetime


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_quiz_instance_list'
    
    def get_queryset(self):
        return QuizInstance.objects.order_by('-pub_date')
    

def create_quiz(request):
    code = None
    
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        
        if form.is_valid():
            
            qtitle = form.cleaned_data['question_title']
            author = form.cleaned_data['creator_name']
            
            print('title : ', qtitle)
            print('author : ', author)
            
            new_quiz_instance = QuizInstance(
                quiz_title = qtitle,
                creator_name = author,
                pub_date = timezone.now(),
                latest_updated_date = timezone.now()
            )

            print('new quiz title : ', new_quiz_instance.quiz_title)
            print('new creator name : ', new_quiz_instance.creator_name)
            print('new quiz date pub : ', new_quiz_instance.pub_date)
            print('new quiz latest date upd : ', new_quiz_instance.latest_updated_date)
            print('new quiz designated code : ', new_quiz_instance.code)
            
            quiz_code = new_quiz_instance.code  
            new_quiz_instance.save()
            
            return redirect('quiz:quiz_success', quiz_code = quiz_code)
        
        
    else:
        form = QuestionForm()
    
    return render(request, 'createquiz.html', {"form" : form})

def success_view(request, quiz_code):
    
    context = {
        'code' : quiz_code
    }
    
    print('got code')
    return render(request, 'makequizsuccess.html', context)
