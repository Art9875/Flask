from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def index():
    return render_template(
        'index.html',
        title='Home page',
    )

@app.route('/1')
def about():
    return render_template(
        'home.html',
        title='Home page',
    )

@app.route('/age', methods=['get', 'post'])
def age():
    if request.method == "POST":
        user_age = request.form['age']
        return f"Вам {user_age}"
    else:
        return "Get запрос"


if __name__ == "__main__":
    app.run(debug=True)
