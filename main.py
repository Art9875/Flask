from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def page():
    return render_template('home.html')

@app.route("/another-page")
def another_page():
    return "Здесь нет денег"

@app.route("/calculate/<n1>/<n2>")
def calculate(n1, n2):
    return f"{n1}*{n2}={int(n1)*int(n2)}"

@app.route("/albums/<int:albums_number><song_number>")
def albums(albums_number, song_number):
    return f"The {albums_number} album and {song_number} musician performer."


if __name__ == "__main__":
    app.run(host='172.0.0.1', port=5000, debug=True)



