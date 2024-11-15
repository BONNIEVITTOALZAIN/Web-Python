from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/fakultas')
def fakultas():
    fakultas = ["FIKR", "FEB"]
    return render_template('fakultas.html' ,fakultas=fakultas )

@app.route('/prodi')
def prodi():
    prodi = [
        {"nama" : "Informatika", "fakultas" : "FIKR"},
        {"nama" : "Elektro", "fakultas" : "FIKR"},
        {"nama" : "MANAJEMEN", "fakultas" : "FEB"},
    ]
    return render_template('prodi.html', prodi=prodi )

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
