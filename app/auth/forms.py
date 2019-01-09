from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User



class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Required(), Length(1, 64),
                                                     Email()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('登录')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[Required(), Length(1, 64),
                                                   Email()])
    username = StringField('Username', validators=[
                 Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                           'Usernames must have only letters, '
                                                                                                     'numbers, dots or underscores')])
    password = PasswordField('Password', validators=[
                 Required(), EqualTo('password2', message='Passwords must match.')])

    password2 = PasswordField('Confirm password', validators=[Required()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')



class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Old password', validators=[Required()])
    password = PasswordField('New password', validators=[Required(), EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Confirm new password', validators=[Required()])
    submit = SubmitField('Update Password')



class PasswordResetRequestForm(FlaskForm):
    email = StringField('Email',validators=[Required(),Length(1,63),Email()])
    submit = SubmitField('重设密码')


class PasswordResetForm(FlaskForm):
    email = StringField('Email',validators=[Required(),Length(1,64),Email()])
    password = PasswordField('新密码',validators=[Required(),EqualTo('password2',message='密码必须匹配')])
    password2 = PasswordField('确认密码',validators=[Required()])
    submit = SubmitField('重设密码')

    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first() is None :
            raise ValidationError('错误的邮箱地址')
































