from flask import Flask, render_template
from models import ArticleModel

application = Flask(__name__)

content = '''

di sini adalah isi contennya cuys
'''

@application.route('/')

def index():
    model = ArticleModel()
    model.setTitle('Apa itu python ')
    model.setDate('10/10/2010')
    model.setContent(content)

    return render_template ('article.html',
        judul = model.getTitle(),
        tanggal = model.getDate(),
        isi = model.getContent()  
    )
    

if __name__ == '__main__':
    application.run(debug=True)