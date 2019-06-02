from flask import Flask, render_template, request, redirect, make_response, session

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    # return redirect('/login')

    

@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == 'POST':
        resp = make_response('ini adalah respon ' + request.form['uname'])
        resp.set_cookie('email_kamu', request.form['uname'])
        return resp
    
    return render_template('login.html')

@app.route('/cokies')
def cokies():
    email = str(request.cookies.get('email_kamu'))
    return 'ini adalah cookies yang tersimpan' + email


if __name__=="__main__":
    app.run(debug=True)