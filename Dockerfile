FROM python:3.8.6

ENV PIP_DISABLE_PIP_VERSION_CHECK=on

RUN pip install poetry

WORKDIR /app
COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction

COPY . /app
RUN python -m ipykernel install --user --name=.venv \
    jupyter nbextension install --py luxwidget \
    jupyter nbextension enable --py luxwidget
CMD ["jupyter", "notebook", "--port=8890", "&"]
