#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
# Модуль dotenv опционален, поэтому убираем зависимость от него
# from dotenv import load_dotenv
# load_dotenv()

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
