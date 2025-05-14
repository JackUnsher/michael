#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request
# Временно отключаем неиспользуемые пока модули для разработки фронтенд-части
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_login import LoginManager
from flask_babel import Babel
# from flask_admin import Admin

from config import config

# Инициализация расширений Flask
# db = SQLAlchemy()
# migrate = Migrate()
# login_manager = LoginManager()
# login_manager.login_view = 'auth.login'
# login_manager.login_message = 'Пожалуйста, войдите для доступа к этой странице.'
babel = Babel()
# admin = Admin(name='Flask Admin', template_mode='bootstrap3')

# Функция для определения текущей локали
def get_locale():
    return request.accept_languages.best_match(['ru', 'en']) or 'ru'

def create_app(config_name='default'):
    """Фабрика приложения Flask."""
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # Инициализация расширений
    babel.init_app(app, locale_selector=get_locale)

    # Регистрация blueprints
    from .public import bp as public_bp
    app.register_blueprint(public_bp)

    # Временно отключаем неиспользуемые пока blueprints
    # from .auth import bp as auth_bp
    # app.register_blueprint(auth_bp, url_prefix='/auth')
    # 
    # from .dashboard import bp as dashboard_bp
    # app.register_blueprint(dashboard_bp, url_prefix='/dashboard')
    # 
    # from .admin import bp as admin_bp
    # app.register_blueprint(admin_bp, url_prefix='/admin')

    return app
