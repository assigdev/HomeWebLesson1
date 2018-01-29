from flask import Flask, render_template

#templates - название папки для шаблонов

app = Flask(__name__)


@app.route('/')
def home():
    context = {
        'author': 'Тененбаум',
        'books': [
            {
                'title': 'Архитектура компьютера',
                'pages': 820
            },
            {
                'title': 'Компьютерные сети',
                'pages': 1020
            },
        ]
    }
    return render_template('home.html', **context)


@app.route('/books/')
def books():
    book_name = 'Архитектура компьютера'
    return render_template('books.html', book_n=book_name)


@app.route('/contact/')
@app.route('/contact/<phone>')
def contact(phone=None):
    if phone is None:
        phone = '656565'
    return 'Мой телефон ' + phone




if __name__ == '__main__':
    app.run(debug=True, port=8001)