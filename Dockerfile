FROM python:3.9-alpine

COPY main.py main.py

CMD ["python", "./main.py"]
