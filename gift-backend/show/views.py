from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Questions
import json


# Create your views here.

def index(request):
    questions = Questions()
    if request.method == 'POST':
        question_text = request.POST.get('question')
        answer_text = request.POST.get('answer')
        questions.questions_text = question_text
        questions.answers = answer_text
        questions.save()

    return render(request, 'show/index.html')


def show_questions(request):
    questions = Questions.objects.filter(answers='这是1')
    dic = {}
    l = []
    for data in questions:
        dic['question'] = data.questions_text
        dic['answer'] = data.answers
        l.append(dic)
    return HttpResponse(dic['answer'])

def ver(request):
    if request.method == 'POST':
        front_question = request.POST.get('question')
        front_ansewr = request.POST.get('answer')
        answer = Questions.objects.filter(questions_text=front_question)
    return render(request, 'show/verification.html')