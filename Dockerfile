FROM openstax/python3-chrome-base

COPY . ./app

WORKDIR ./app

ENV PYTHONPATH "${PYTHONPATH}:./app"

RUN pip install poetry

RUN poetry config virtualenvs.in-project true
RUN poetry install

RUN ./.venv/bin/python -m playwright install
RUN ./.venv/bin/python -m playwright install-deps

RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
