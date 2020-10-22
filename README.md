# OpenAPI 3 Generator

The goal of this project is to create a generator in Python to conveniently create
API definitions using OpenAPI 3 structure and then to inject the generated YAML file
both with Swagger UI to a project.

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

If you are prototyping your API then run Flask with Swagger UI and start
the job by editing schemas and paths:

```bash
make run

# * Running on http://127.0.0.1:8060/ (Press CTRL+C to quit)
# * Restarting with stat
# * Debugger is active!
```

Go to http://127.0.0.1:8060 in your browser.

<img src="./examples/screen.png" width="600">
 