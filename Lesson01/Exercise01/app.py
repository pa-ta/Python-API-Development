from flask import Flask

app = Flask(__name__) # If you are using a single module, __name__ is always the correct value.
# If you however are using a package, it’s usually recommended to hardcode the name of your package there.
# For more information: https://flask-russian-docs.readthedocs.io/ru/0.10.1/api.html#flask.Flask

@app.route("/")  #http://127.0.0.1:5000/
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run()