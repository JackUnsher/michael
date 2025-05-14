#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template, current_app, request, flash, redirect, url_for
from . import bp
from .forms import ContactForm

@bp.route('/')
def index():
    return render_template('public/index.html', title='Главная')

@bp.route('/about')
def about():
    return render_template('public/about.html', title='О нас')

@bp.route('/send-contact', methods=['POST'])
def send_contact():
    form = ContactForm()
    if form.validate_on_submit():
        # В реальном приложении здесь будет код для отправки email
        # или сохранения данных в базу данных
        flash('Ваше сообщение успешно отправлено!', 'success')
        return redirect(url_for('public.index') + '#contact')
    
    # Если форма не прошла валидацию, возвращаемся на страницу с формой
    for field, errors in form.errors.items():
        for error in errors:
            flash(f"{getattr(form, field).label.text}: {error}", 'error')
    
    return redirect(url_for('public.index') + '#contact')
