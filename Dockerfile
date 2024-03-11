FROM python:3.8

RUN mkdir /app
WORKDIR /app
COPY . /app

RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false --local

RUN poetry install

CMD ["python3", "metamask_bf_v2.py"]
