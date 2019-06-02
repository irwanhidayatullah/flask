from flask import Flask, render_template, request
from models import *
 
application = Flask(__name__)
@application.route('/')
def index():
    return render_template('index.html')

@application.route('/about/')
def about():
    # Mendefinisikan variable disini
    ini_var = 'Python dan Flask '
    int_var = 123456789
    float_var = 123.2
    list_var = [10,20,30]
    dict_var = {'angka' : 1, 'nama': 'irwan'}
    model = Lingkaran(5.0)
    
    # ini cara membuat dictionary
    menu = { '/' : 'home', 'buah':'nanas', 'kendaraan':'mobil', 'laptop':'lenovo','google.com':'www.google.com'}
      
    # model = model itu maksudnya adalah variable apa saja yang akan di kirim ke template
    return render_template('about.html', 
        str_var = ini_var, 
        int_var=int_var, 
        float_var=float_var, 
        list_var=list_var, 
        dict_var=dict_var,  
        model = model,
        menu = menu )
  

@application.route('/login', methods=['GET','POST'])
def show_login():
    if request.method == 'POST':
        return "ini menggunakan POST" + request.form['Username']
    else:
        return "ini menggunakan GET" + request.form['Username']
    return render_template('login.html')

if __name__=='__main__':
    application.run(debug=True)