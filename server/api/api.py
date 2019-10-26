from flask import Flask

app = Flask("server")


@app.route('/')
def hello():
    return 'Test'


def run_api():
    app.run(debug=True, host='localhost', port=5000)
