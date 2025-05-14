#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from ..models import User
from flask import current_app

class ProfileForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[
        DataRequired(),
        Length(1, 64)
    ])
    language = SelectField('Язык', choices=[('ru', 'Русский'), ('en', 'English')])
    submit = SubmitField('Обновить')

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.original_username = None

    def validate_username(self, field):
        from flask_login import current_user
        if field.data != current_user.username:
            if User.query.filter_by(username=field.data).first():
                raise ValidationError('Имя пользователя уже занято.')
