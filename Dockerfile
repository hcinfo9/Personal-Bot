FROM python:3.11.9 as builder

COPY . .

RUN pip install Flask

RUN pip install google-generativeai

RUN pip install --upgrade google-generativeai

WORKDIR /app

EXPOSE 5000

ENTRYPOINT ["python", "main.py"]

