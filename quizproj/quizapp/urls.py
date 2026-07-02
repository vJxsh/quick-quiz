from . import views
from django.urls import path

app_name = 'quiz'

urlpatterns = [
    path('',views.IndexView.as_view(), name = 'index'),
    path('create_quiz/', views.create_quiz, name = 'createquiz'),
    path('success_create/<str:quiz_code>/', views.success_view, name='quiz_success'),
    path('delete_quiz_instance/<int:quiz_instance_id>/', views.delete_quiz_instance, name='delete_quiz')
]
