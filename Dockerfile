FROM python:3.11.9-alpine3.20

COPY . /app

RUN pip install google-generativeai

RUN pip install --upgrade google-generativeai

WORKDIR /app

EXPOSE 5000

CMD python main.py