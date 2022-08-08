from python:3.8 as base

# let's create a folder to work from 
workdir /code

# copy over our requirements
copy ./requirements.txt /code/requirements.txt

# install the python deps
run pip install --no-cache-dir --upgrade -r /code/requirements.txt

# copy over our source folder
copy ./src/ /code/



from base as api-tests

# copy over tests
copy ./tests/ /code/tests/

# install test requirements
run pip install -r /code/tests/requirements.txt

# run pytest
cmd ["python", "-m", "pytest", "tests/"]



from base as local-serve

# serve on local host
cmd ["python", "uvicorn_serve.py"]