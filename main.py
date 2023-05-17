from flask import Flask
app = Flask(__name__)
print(__name__)

def make_bold(function):
    def wrapper_function():
        text = function()
        return f'<b>{text}</b>'
    return wrapper_function

def make_emphasis(function):
    def wrapper_function():
        text = function()
        return f'<em>{text}</em>'
    return wrapper_function

def make_underline(function):
    def wrapper_function():
        text = function()
        return f'<u>{text}</u>'
    return wrapper_function


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route("/bye")
@make_bold
@make_underline
@make_emphasis
def bye():
    return "Bye"

@app.route("/<name>")
def greet(name):
    return f'<h1 style="text-align: center">"Hello there {name}"</h1>' \
           f'<p>this is a paragraph</p>' \
           f'<img src="https://media.giphy.com/media/C23cMUqoZdqMg/giphy.gif" width=300px>'


if __name__ == "__main__":
    app.run(debug=True)