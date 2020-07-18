from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Questions, Score
from giftbackend import settings
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import json

serializer = Serializer(settings.SECRET_KEY, expires_in=3600)


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
    token = request.headers['Authorization']
    try:
        serializer.loads(token)
        questions = list(Questions.objects.order_by('id').values())
        return JsonResponse({'data': questions})
    except:
        return JsonResponse({'data': 'Unauthorized'})
    # questions = list(Questions.objects.order_by('id').values())
    # return JsonResponse({'data': questions})


def get_score(request):
    token = request.headers['Authorization']
    try:
        serializer.loads(token)
        score = Score.objects.filter(id=0).values()
        data = list(score)[0]['total_score']
        return JsonResponse({'data': data})
    except:
        return JsonResponse({'data': 'Unauthorized'})


def change_score(request):
    if request.method == 'POST':
        score = request.POST.get('score')
        new_score = Score.objects.get(id=0)
        new_score.total_score = score
        new_score.save()
        return JsonResponse({'code': 200})


def ver(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        passwd = request.POST.get('passwd')
        user_info = {'username': username, 'passwd': passwd}
        # 生成token
        token = serializer.dumps(user_info).decode()
        # 用户认证
        user = authenticate(request, username=username, password=passwd)
        if user is not None:
            # 登陆
            login(request, user)
            data = {'code': 200, 'token': token}
            return JsonResponse(data)
        else:
            return JsonResponse({'status': "error"})
