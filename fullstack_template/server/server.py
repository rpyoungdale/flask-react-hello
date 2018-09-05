from flask import Flask, render_template, url_for

app = Flask(__name__, static_folder="../static/dist", template_folder="../static")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return "Hello Ryan!"

if __name__ == '__main__':
    app.run(debug=True, port=3000)
