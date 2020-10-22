from flask import Flask, render_template
from source.project import spec

app = Flask(__name__)


@app.route('/swagger.yaml')
def swagger_yaml():
    return spec.to_yaml()


@app.route('/')
def index():
    return render_template('swagger_ui.html', url='http://127.0.0.1:8060/swagger.yaml')
