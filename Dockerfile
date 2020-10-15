FROM python:3.7-alpine
WORKDIR /app
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev 

RUN pip install --upgrade pip

COPY ./Pipfile ./
RUN pip install pipenv
RUN pipenv lock --requirements > requirements.txt
RUN pip install -r requirements.txt

COPY ./ ./

CMD [ "gunicorn", "--bind", ":8080", "--workers", "3", "trackerproject.wsgi:application"]