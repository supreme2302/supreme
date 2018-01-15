# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.db import connection
from questions.models import Question
import MySQLdb
#	Открываем соединение
db = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="1",
    db="zakaz"
)
db.set_character_set('utf8')

#	Получаем курсор для работы с БД
c = db.cursor()
c.execute('SET NAMES utf8;')
c.execute('SET CHARACTER SET utf8;')
c.execute('SET character_set_connection=utf8;')
#	Выполняем вставку
c.execute("INSERT INTO zakaz (name, description) VALUES (%s, %s);", ('Книга', 'Описание книги'))
#	Фиксируем изменения
db.commit()
#	Выполняем выборку
c.execute("SELECT * FROM zakaz;")
#	Забираем все полученные записи #
entries = c.fetchall()
#	И печатаем их
for e in entries:
    print(e)
#c.сlose() # Закрываем курсор
db.close() # Закрываем соединение