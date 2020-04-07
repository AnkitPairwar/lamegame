from flask-wtf import FlaskForm
from wtform import StringField, PasswordField, SubmitField, RememberField
from wtform.validators import DataRequired ,Length ,Email ,EqualTo

class RegitrationForm(FlaskForm):
    username = StringField('Username' , validators = [
        DataRequired() , 
        Length( min = 3 , max = 20 )
        ])
    email = StringField('email' , validators = [
        DataRequired(),
        Email()
        ])
    password = PasswordField( 'Password' ,validators = [
        DataRequired()
        ])
    confirm_password = PasswordField( 'Confirm Password' ,validators =[
        DataRequired(),
        EqualTo('password')
        ])
    Submit = SubmitField('Sign Up')                                

class LoginForm(FlaskForm):
    email = StringField('email' , validators = [
        DataRequired(),
        Email()
        ])
    password = PasswordField( 'Password' ,validators = [
        DataRequired()
        ])
    Remember = BooleanField('Remember Me')        
    Submit = SubmitField('Log In')        