from flask import Flask,render_template ,url_for
from forms import LoginForm , RegitrationForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '8e0210ea0fd90f6860946046fcd0036a'

posts = [
    {
        'author':'Ankit',
        'content':'First commment',
        'date':'21'
    },

    {
        'author':'Pairwar',
        'content':'Second comment',
        'date':'21' 
    }
]

@app.route("/")
@app.route("/home")
def hello():
    return render_template('index.html' , posts = posts , title = 'homepage'
    )

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/register")
def register():
    form = RegitrationForm()
    return render_template('register.html' ,title = 'register' ,form = form)

@app.route("/login")
def register():
    form = LoginForm()
    return render_template('login.html' ,title = 'login' ,form = form)

if __name__ == '__main__':
    app.run(debug=True)    