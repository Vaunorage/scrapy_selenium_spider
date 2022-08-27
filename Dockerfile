FROM python:3.8-slim-buster

RUN sudo apt-get update && sudo apt-get install -y libpq-dev curl python3 python3-pip
RUN sudo -H pip install poetry

COPY . .

RUN oetry config virtualenvs.in-project true
RUN poetry install
RUN poetry shell

CMD [ "python", "./tunisie/main.py"]