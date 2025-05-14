#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class UserForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired(), Length(1, 64)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    role = SelectField('Роль', choices=[('user', 'Пользователь'), ('admin', 'Администратор')])
    language = SelectField('Язык', choices=[('ru', 'Русский'), ('en', 'English')])
    is_active = BooleanField('Активен')
    submit = SubmitField('Сохранить')
