FROM python:3.8

WORKDIR /usr/src/app

RUN pip install pipenv

COPY . .

RUN pipenv install --system --deploy

ENTRYPOINT [ "python" ]
