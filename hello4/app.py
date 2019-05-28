
from flask import Flask, render_template
from models import HelloModel


application = Flask(__name__)

@application.route('/')
def index():
    model = HelloModel()
    return render_template ('hello.html', model=model)


if __name__=='__main__':
    application.run(debug=True)