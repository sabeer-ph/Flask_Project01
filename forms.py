# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 13:32:52 2022

@author: husssabe
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AddTaskForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    submit = SubmitField('Submit')