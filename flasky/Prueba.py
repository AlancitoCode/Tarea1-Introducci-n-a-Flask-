from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

def hello():
    print('test')

if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='Manage your Flask application')
    parser.add_argument('command', choices=['hello'], help='Command to execute')
    args = parser.parse_args()

    if args.command == 'hello':
        hello()
    else:
        print('Invalid command')