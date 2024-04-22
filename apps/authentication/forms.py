# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from flask_wtf import Form

from wtforms import StringField, PasswordField
# from wtforms.validators import Required

from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import SubmitField
# from wtforms import StringField, 
from wtforms.validators import Email, DataRequired

# login and registration


class LoginForm(FlaskForm):
    username = StringField('Username',
                         id='username_login',
                         validators=[DataRequired()])
    password = PasswordField('Password',
                             id='pwd_login',
                             validators=[DataRequired()])


class CreateAccountForm(FlaskForm):
    username = StringField('Username',
                         id='username_create',
                         validators=[DataRequired()])
    email = StringField('Email',
                      id='email_create',
                      validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             id='pwd_create',
                             validators=[DataRequired()])

class UploadForm(FlaskForm):
    file = FileField('File'),
    submit = SubmitField('Submit')
    # username = StringField('Username',
    #                      id='username_login',
    #                      validators=[DataRequired()])
 
