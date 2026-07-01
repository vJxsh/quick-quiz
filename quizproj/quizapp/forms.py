from django import forms

class QuestionForm(forms.Form):
    creator_name = forms.CharField(label = 'Enter your name', max_length=128)
    question_title = forms.CharField(label = 'Enter Quiz Title', max_length=64)