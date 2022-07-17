# the dockerfile is for localhost testing and pytest
FROM python:3.8

WORKDIR /code
 
COPY ./requirements.txt /code/requirements.txt
 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
 
COPY ./src/ /code/

# run as local server
CMD ["python", "uvicorn_serve.py"]