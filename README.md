# OpenAPI 3 Generator

The goal of this project is to create a generator that conveniently creates
API definitions in OpenAPI 3 format and then injects the generated YAML file
with Swagger UI to any project.

### How to use?

To create a `api.yaml` file:

```bash
# install all dependencies
pipenv install

# enter the environment
pipenv shell

# create a YAML definition
python build.py
```

If you are prototyping your API then run a Flask app with Swagger UI using [GNU make](https://www.gnu.org/software/make/) and start
to create your API by editing schemas and paths:

```bash
make run

# * Running on http://127.0.0.1:8060/ (Press CTRL+C to quit)
# * Restarting with stat
# * Debugger is active!
```

You can find Swagger UI on http://127.0.0.1:8060 in your browser.

Demo:

<img src="./examples/screen.png" width="800">
 