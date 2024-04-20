from flask import Flask, render_template, url_for

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('new.html')



@app.route('/home')
def home():
    return render_template('home.html')



@app.route('/home/atc')
def atc():
    return render_template('atc.html')


if __name__ == '__main__':
    app.run(debug=True)
