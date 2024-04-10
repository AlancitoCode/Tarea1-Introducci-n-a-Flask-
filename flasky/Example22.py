from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'
@app.route('/user/<Alan>')
def user(Alan):
 return '<h1>Hello, %s!</h1>' % Alan

if __name__ == '__main__':
 app.run(debug=True)

