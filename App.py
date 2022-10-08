# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 19:24:13 2022

@author: husssabe
"""
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)

from routes import *


if __name__ == '__main__':
    app.run(debug=True)
