from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Questions
from giftbackend import settings
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
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
    # questions = Questions.objects.filter(answers='这是1')
    # dic = {}
    # l = []
    # for data in questions:
    #     dic['question'] = data.questions_text
    #     dic['answer'] = data.answers
    #     l.append(dic)
    # return HttpResponse(dic['answer'])
    questions = {'1': [{'question': '我们的纪念日'}, {'answer': '20170715'}], '2': [{'question': '我的生日'}, {'answer': '19980720'}]}

    return JsonResponse(questions)

def ver(request):
    serializer = Serializer(settings.SECRET_KEY, expires_in=3600)
    if request.method == 'POST':
        username = request.POST.get('username')
        passwd = request.POST.get('passwd')
        user_info = {'username': username, 'passwd': passwd}
        # 生成token
        token = serializer.dumps(user_info).decode()
        # 用户认证
        user = authenticate(request,username=username, password=passwd)
        if user is not None:
            # 登陆
            login(request,user)
            data = {'code': 200, 'token': token}
            return JsonResponse(data)
        else:
            return JsonResponse({'status': "error"})