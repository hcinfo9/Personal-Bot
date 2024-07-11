FROM python:3.11.9

WORKDIR /app

COPY . .

RUN pip install Flask

RUN pip install google-generativeai

EXPOSE 5000

CMD ["python", "main.py"]

