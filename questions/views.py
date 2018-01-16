# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse

from django.contrib import auth
from questions.forms import *
from questions.models import ModelAskForm, Like


#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from questions.paginator import paginate

from django.contrib.auth.models import User
from models import Question, Profile
from fill import *


# def pagination(object_list, request, count_per_page):
#     paginator = Paginator(object_list, count_per_page)
#     page = request.GET.get('page')
#
#     try:
#         return paginator.page(page)
#     except PageNotAnInteger:
#         return paginator.page(1)
#     except EmptyPage:
#         return  paginator.page(paginator.num_pages)





# Create your views here.
def Questions(request):
    questions = Question.objects.all()
    page = request.GET.get('page')
    return render(request, 'questions.html', {'questions': questions, 'data': paginate(questions, page)})



def tag(request):
    tagg = Tag.objects.get(name=request.GET.get('tag'))
    data = Question.objects.filter(tag=tagg)
    print data
    page = request.GET.get('page')
    #for i in Question.objects.all().filter(tag=tagg):
        #data.append(i)
    return render(request, 'questions.html', {'paginator': paginate(data, page)})

def ListingByTag(request):
    questions = Question.objects.all()

    page = request.GET.get('page')
    return render(request, 'questions.html', {'questions': questions, 'paginator': paginate(questions, page)})


def NewQuestion(request):
    if request.method == 'POST':
        tag_form = ModelAskForm(request.POST)
        #is_val_for_ModelAskForm = tag_form.is_valid()
        #data_tag = tag_form.cleaned_data
        tags = request.POST.get('tags').split(' ')
        form = AskForm(request.POST)
        is_val = form.is_valid()
        data = form.cleaned_data
        if is_val:
            print 'ok'
            new_q = Question.objects.create(
                user = request.user.profile,
                title = data['title'],
                text = data['text'],
                #tag = data_tag,
                #tag = data['tags'],
                rating = 0,
            )
            new_q.save()
            for i in tags:
                try:
                    tagg = Tag.objects.get(name=i)
                    new_q.tag.add(tagg)
                except:
                    tagg = Tag(name=i)
                    tagg.save()
                    new_q.tag.add(tagg)
                new_q.save()
            return HttpResponseRedirect('/')
    else:
        form = AskForm()
        tag_form = ModelAskForm()

    return render(request,'new question.html', {'form': form, 'tag_form': tag_form})

def OneQuestion(request, qnum):
    quest = Question.objects.get(id=qnum)
    page = request.GET.get('page')
    answ = Answer.objects.filter(question=quest)

    if request.user.is_authenticated:
        #us = request.user
        if request.method == 'POST':

            form = AnswerForm(request.POST)
            is_val = form.is_valid()
            data = form.cleaned_data
            t = data['text']
            print '____________________'
            print t
            print request.user.profile
            print quest
            if is_val:
                answer = Answer.objects.create(
                    user = request.user.profile,
                    question = quest,
                    text = data['text'],
                )
                answer.save()

                return HttpResponseRedirect(qnum)
        else:
            form = AnswerForm()
    else:
        return HttpResponseRedirect('/sign_in/')
    return render(request, 'one_question.html', {'questions': quest, 'paginator': paginate(answ, page), 'form': form})






def Registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        is_val = form.is_valid()
        data = form.cleaned_data
        avatar = request.FILES.get('file')

        if data['password'] != data['password2']:
            is_val = False
            form.add_error('password2', ['Пароли должны совпадать'])
        if User.objects.filter(username=data['login']).exists():
            form.add_error('username', ['Такой логин уже занят'])
            is_val = False

        if is_val:
            data = form.cleaned_data
            user = User.objects.create_user(data['login'], data['email'], data['password'])
            print(user)
            profile = Profile.objects.create(user=user, nickname=data['username'], avatar=avatar)
            profile.save()

            return HttpResponseRedirect('/')
    else:
        form = RegistrationForm()

    return render(request, 'regist.html', {'form': form})


def test(request):
    if request.method == 'POST':
        login_name = request.POST.get('login')
        password_name = request.POST.get('password')
        # user = authenticate(request, username=login, password=password)
        # if user is not None and user.is_active:
        #     login(request, user)
        #     return HttpResponseRedirect('/')
        user = authenticate(request, username=login_name, password=password_name)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/test/')

    return render(request, 'test.html', locals())

def Settings(request):
    if request.user.is_authenticated:
        us = request.user
        if request.method == 'POST':
            login = request.POST.get('login')
            email = request.POST.get('email')
            username = request.POST.get('nickname')
            avatar = request.FILES.get('file')
            us.username= login
            us.profile.nickname = username
            us.profile.avatar = avatar
            us.save()
            us.profile.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/sign_in/')



    return render(request,'settings.html',locals())




def Hot(request):
    data = []

    for i in xrange(1, 30):
        data.append(
            {
                'title': 'title' + str(i),
                'text': 'text' + str(i),
                'likecount': i % 20,
            }
        )

    data.sort(key=lambda  x: x["likecount"], reverse=True)


    page = request.GET.get('page')
    return render(request, 'questions.html', {
        'hot':True,
        'questions': data,
        'paginator': paginate(data, page),
    })





def Login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        print(form)
        data = form.cleaned_data
        is_val = form.is_valid()

        if form.is_valid():
            user = authenticate(request, username=data['username'], password=data['password'])
            # user = authenticate(request, username='petrov',password='12345678')
            print(len(data['username']), len(data['password']))
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                form.add_error('username', ['Неверный логин или пароль'])
                is_val = False

                # raise forms.ValidationError('Имя пользователя и пароль не подходят')

    else:
        form = LoginForm()

    return render(request, 'sign_in_dj.html', {'form': form})


def Logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')

def like(request):
    if request.method == 'POST':
        user = request.user
        quest = Question.objects.get(id=int(request.POST.get('question')))
        if request.POST.get('positive') == 'true':
            print('positive')
            try:
                lk = Like(question_key=quest, like_author=user, rate=True)
                lk.save()
                quest.counter()
                quest.save()
                return JsonResponse({'rating': quest.rating}, status=200)
            except:
                lkk = Like.objects.get(question_key=quest, like_author=user, rate=True)
                lkk.delete()
                quest.counter()
                quest.save()
                return JsonResponse({'rating': quest.rating}, status=200)


        else:
            try:
                lk = Like(question_key=quest, like_author=user, rate=False)
                lk.save()
                quest.counter()
                quest.save()
                return JsonResponse({'rating': quest.rating}, status=200)
            except:
                lkk = Like.objects.get(question_key=quest, like_author=user, rate=False)
                lkk.delete()
                quest.counter()
                quest.save()
                return JsonResponse({'rating': quest.rating}, status=200)
    return HttpResponse()


def scroll(request):
    print('inscroll')
    data = Question.objects.all()
   # page = paginate(data, request)
    page = request.GET.get('page')
    print page

    print('pagination done')
    return render(request, 'list.html', {'data': paginate(data, page)})


