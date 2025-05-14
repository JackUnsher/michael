#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, TelField, BooleanField
from wtforms.validators import DataRequired, Email, Optional

# Форма обратной связи
class ContactForm(FlaskForm):
    name = StringField('Ваше имя', validators=[DataRequired()])
    email = StringField('Ваш Email', validators=[DataRequired(), Email()])
    phone = TelField('Ваш телефон', validators=[Optional()])
    message = TextAreaField('Ваше сообщение', validators=[DataRequired()])
    consent = BooleanField('Я согласен на обработку персональных данных', validators=[DataRequired()])
    submit = SubmitField('Отправить сообщение')
