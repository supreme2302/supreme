# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from questions.models import Question, Answer, Tag, Profile, Like

def count(obj):
    return Question.objects.filter(user=obj).count()

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar', count)
    list_filter = ('user', )
    search_fields = ('user', )

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Tag)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Like)