#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint

bp = Blueprint('public', __name__)

from . import routes
