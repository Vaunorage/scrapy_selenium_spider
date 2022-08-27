FROM python:3.8-slim-buster

COPY . ./app

WORKDIR ./app

ENV PYTHONPATH "${PYTHONPATH}:./app"


RUN apt-get update && apt-get install -y libpq-dev curl python3 python3-pip
RUN pip install poetry

RUN poetry config virtualenvs.in-project true
RUN poetry install

RUN chmod +x ./entrypoint.sh
RUN chmod +x ./cmd_playwright.sh

ENTRYPOINT ["./entrypoint.sh"]
