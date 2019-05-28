from flask import Flask

application = Flask(__name__)


@application.route('/')
def index():
    return 'hello world'

@application.route('/hello/<name>')
def hello(name):
    return ' hello %s' %name

@application.route('/page/<int:number>')
def page(number):
    return '<h2> Page#%d ' %number
    
if __name__=='__main__':
    application.run(debug=True)