from flask import Flask, render_template, request
from models import Lingkaran

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == "POST":
        model = Lingkaran()
        model.setRadius(request.form['radius'])
        return render_template('lingkaran.html', model=model)
    else:
        return render_template('form.html')

if __name__ == "__main__":
    app.run(debug=True)
