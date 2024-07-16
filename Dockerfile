FROM python:3.11.9 as builder

WORKDIR /app

COPY ./ /app

RUN pip install Flask

RUN pip install google-generativeai

RUN pip install --upgrade google-generativeai

EXPOSE 5000

CMD ["python", "main.py"]
