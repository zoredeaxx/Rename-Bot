from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Server Healthy'


if __name__ == "__main__":
    app.run()
