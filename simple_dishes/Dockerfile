FROM python:3.10-slim
WORKDIR /app
COPY simple_dishes .
RUN pip3 install -r requirements.txt --no-cache-dir
CMD ["gunicorn", "simple_dishes.wsgi:application", "--bind", "0:8000"]