FROM python:3.10-slim

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

COPY ./docker-scripts/entrypoint.sh ./docker-scripts/start.sh /

WORKDIR /home/

COPY requirements.txt /home/
RUN pip install -r requirements.txt
