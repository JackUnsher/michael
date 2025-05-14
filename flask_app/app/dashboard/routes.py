#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from . import bp
from .forms import ProfileForm
from .. import db

@bp.route('/')
@login_required
def index():
    return render_template('dashboard/index.html', title='Панель управления')

@bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = ProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.language = form.language.data
        db.session.commit()
        flash('Ваш профиль успешно обновлен.')
        return redirect(url_for('dashboard.profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.language.data = current_user.language
    
    return render_template('dashboard/profile.html', title='Профиль', form=form)
