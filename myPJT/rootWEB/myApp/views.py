from django.shortcuts import render, redirect
from .models import *
# Create your views here.

#첫 화면 접속
#로그인 시 기존 세션 유지
def index(request) :
    print(">>>>>> debug client path : index/, index(), render index.html")

    if request.session.get('session_user_id'):
        context = {}
        context['id'] = request.session['session_user_id']

        return render(request, 'main.html', context)

    return render(request, 'index.html')

#회원가입 기능
def joinForm(request) :
    print(">>>>>> debug client path : joinForm/, joinForm(), render joinForm.html")
    return render(request, 'joinForm.html')

def join(request) :
    print(">>>>>> debug client path : join/, join(), redirect index.html")
    id = request.POST['id']
    pwd = request.POST['pwd']

    user_tbl(user_id=id, user_pwd=pwd).save()

    return redirect('index')


#로그인 기능
def login(request) :
    print(">>>>>> debug client path : login/, login(), render main.html")
    id = request.POST['id']
    pwd = request.POST['pwd']

    user = user_tbl.objects.get(user_id = id, user_pwd =pwd)

    request.session['session_user_id'] = user.user_id

    context = {}
    context['id'] = request.session['session_user_id']


    return render(request, 'main.html', context)

#로그아웃 기능
def logout(request) :
    print(">>>>>>debug, client paht: logout/, logout(), render index.html")
    request.session['session_user_id'] = {}
    return redirect('index')


#게시판
def board(request) :
    print(">>>>>> debug client path : board/, board(), render board.html")
    # boards = board_tbl.objects.all()
    # context = {'boards' : boards}
    return render(request, 'board.html')

def bbsForm(request) :
    print(">>>>>> debug client path : bbsForm/, bbsForm(), render bbsForm.html")
    return render(request, 'bbsForm.html')


def register(request) :
    title = request.POST['title']
    content = request.POST['content']
    writer = request.POST['writer']

    user = user_tbl.objects.get(user_id=writer)
    board_tbl(title = title, content = content, writer = user).save()
    return redirect('board')


#지도
def map(request) :
    print(">>>>>debut, client path : map/, map(), render map.html")
    cities = city_tbl.objects.all()

    weathers = weather_tbl.objects.all()


    context = {'cities' : cities, 'weathers' : weathers}
    return render(request, 'map.html', context)

#날씨
def weather(request) :
    print(">>>>>debut, client paht : weather/ weather(), render weather.html")
    id = request.GET['id']

    weathers = weather_tbl.objects.all()
    weather = weather_tbl.objects.get(id=id)
    context = {'weather' : weather, 'weathers' : weathers}
    return render(request, 'weather.html', context)

def cloth(request) :
    print(">>>>>>debut, client path : cloth/ cloth(), redner cloth.html")
    weather = weather_tbl.objects.all()
    combination = combination_tbl.objects.all()
    context = {'weather' : weather, 'combination' : combination}

    return render(request, 'cloth.html', context)