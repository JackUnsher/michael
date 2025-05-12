from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def main_desktop():
    return render_template('main_desktop.html')

@app.route('/tablet')
def main_tablet():
    return render_template('main_tablet.html')

@app.route('/mobile')
def main_mobile():
    return render_template('main_mobile.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 