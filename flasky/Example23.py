
'''
PARA QUE FUNCIONE ESTE EJEMPLO DEBEMOS DESCARGAR ESTAS VERSIONES Y TENER PYTHON 
VERSION ANTERIOR YA QUE Esta función inspect.getargspec() 
es parte de la biblioteca estándar de Python, pero ha quedado obsoleta desde Python 3
 click==7.1.2
 colorama==0.4.4
 Flask==1.1.4
 Flask-Script==2.0.6
 itsdangerous==1.1.0
 Jinja2==2.11.3
 MarkupSafe==2.0.1
 Werkzeug==1.0.1
'''
from flask_script import Manager
from Prueba import app
from flask import Flask
manager = Manager(app)
@manager.command
def hello():
     print('test')

if __name__ == "__main__":
     manager.run()