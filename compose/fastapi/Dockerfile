FROM python:3.10

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt update && apt upgrade -y

RUN apt install -y -q build-essential python3-pip python3-dev
RUN pip3 install -U setuptools wheel
RUN pip3 install gunicorn uvloop httptools

COPY Pipfile .
COPY Pipfile.lock .

COPY /service/* /app/

RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

COPY ./compose/fastapi/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

ENV ACCESS_LOG=${ACCESS_LOG:-/proc/1/fd/1}
ENV ERROR_LOG=${ACCESS_LOG:-/proc/1/fd/2}

WORKDIR /app

ENV PYTHONPATH "${PYTHONPATH}:/app"
ENTRYPOINT ["/start"]