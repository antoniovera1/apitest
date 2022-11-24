FROM python:3.8.10
ENV PYTHONBUFFERED 1
WORKDIR /code

COPY requirements.txt /code/requirements.txt
RUN python3 -m pip install -r requirements.txt
COPY . /code/

CMD python3 manage.py runserver 0.0.0.0:8000