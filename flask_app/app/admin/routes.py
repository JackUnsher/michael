#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from . import bp
from .. import admin, db
from ..models import User
from .forms import UserForm
from flask_admin.contrib.sqla import ModelView

# Регистрация моделей в админке
class UserAdmin(ModelView):
    column_searchable_list = ('username', 'email')
    column_filters = ('username', 'email', 'role', 'is_active')
    form_excluded_columns = ('password_hash', 'created_at', 'updated_at')
    column_exclude_list = ('password_hash',)
    can_create = True
    can_edit = True
    can_delete = True
    
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin()
    
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login', next=request.url))


# Добавление моделей в админку
admin.add_view(UserAdmin(User, db.session))

@bp.route('/')
@login_required
def index():
    if not current_user.is_admin():
        flash('У вас нет доступа к этой странице.')
        return redirect(url_for('dashboard.index'))
    return render_template('admin/index.html', title='Админ-панель')
