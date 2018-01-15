# -*- coding: utf-8 -*-
from __future__ import unicode_literals



from django.db import models
from datetime import datetime
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django import forms
import math



#GOOD_RATING = 10

class Question(models.Model):
    user = models.ForeignKey('Profile')
    title = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.IntegerField(default=0)
    pub_date = models.DateTimeField(default=timezone.now)
    tag = models.ManyToManyField('Tag')

    def counter(self):
        self.rating = int((Like.objects.filter(question_key=self, rate=True).count() - Like.objects.filter(question_key=self, rate=False).count()))

    def __unicode__(self):
        return "{} {} {} {}".format(self.id, self.title, self.rating, self.pub_date)

class Answer(models.Model):
    user = models.ForeignKey('Profile')
    question = models.ForeignKey('Question')
    text = models.TextField()
    rating = models.IntegerField(default=0)
    correct = models.BooleanField(default=False)
    pub_date = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return "{} {}".format(self.question.title, self.pub_date)

class Tag(models.Model):
    name = models.CharField(max_length=255)


    def __unicode__(self):
        return "{}".format(self.name)


class Profile(models.Model):
    user = models.OneToOneField(User)
    nickname = models.CharField(max_length=255, default=0)
    avatar = models.ImageField(upload_to='uploads', null=True, blank=True)

    def __unicode__(self):
        return "{}".format(self.nickname)



class Like(models.Model):
    question_key = models.ForeignKey(Question)
    like_author = models.ForeignKey(User)
    rate = models.BooleanField(default=None)

    class Meta:
        unique_together= ['question_key', 'like_author']



class ModelAskForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['tag']
        widgets = {
            #'tag': forms.Select(attrs={'class': 'form-control'}),
        }

