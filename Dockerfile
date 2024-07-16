FROM mateusoliveira43/poetry:1.5-python3.11-slim-bullseye

WORKDIR /tmp/
COPY ./pyproject.toml ./poetry.lock /tmp/
RUN poetry install
COPY . .
ENTRYPOINT [ "poetry", "run", "pytest", "tests/" ]
