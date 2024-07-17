FROM mateusoliveira43/poetry:1.5-python3.11-slim-bullseye

WORKDIR /tmp/
COPY ./pyproject.toml ./poetry.lock /tmp/
RUN poetry install

RUN set -xe \
    && apt-get update  \
    && apt-get install -y --no-install-recommends \
       netcat \
    && apt-get clean
COPY . .
#ENTRYPOINT [ "poetry", "run", "pytest", "tests/" ]
