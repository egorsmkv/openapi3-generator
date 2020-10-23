from flask import Flask, render_template
from api.project import spec, requests
from internal.helpers import add_request_bodies

app = Flask(__name__, template_folder='misc/templates')


@app.route('/swagger.yaml')
def swagger_yaml():
    return add_request_bodies(spec, requests)


@app.route('/')
def index():
    return render_template('swagger_ui.html', url='http://127.0.0.1:8060/swagger.yaml')
