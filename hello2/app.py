from flask import Flask
from models import HelloModel

application = Flask(__name__)

@application.route('/')
def index():
    model = HelloModel()
    return model.getText

if __name__=='__main__':
    application.run(debug=True)