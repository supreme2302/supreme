from django.conf.urls import url, include
from django.contrib import admin
from questions import views

urlpatterns = [
    url(r'^hot/', views.Hot, name='hot'),
    url(r'^$', views.Questions, name='question'),
    url(r'^listing_by_tag/', views.tag, name='listing_by_tag'),
    url(r'^new_question/', views.NewQuestion, name='new_question'),
    #url(r'^one_question/', views.OneQuestion, name='one_question'),
    url(r'^registration/', views.Registration, name='registration'),
    url(r'^settings/', views.Settings, name='settings'),
    url(r'^sign_in/', views.Login, name='sign_in'),
    url(r'^logout/', views.Logout, name='logout'),
    url(r'^test/', views.test, name = 'test'),
    url(r'^one_question/(?P<qnum>(\d+))$', views.OneQuestion,  name="one_question"),
    url(r'^like', views.like, name='like'),
]
