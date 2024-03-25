FROM python:3.12.2

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080


CMD ["python", "example_app/app.py"]