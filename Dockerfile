FROM python:3-alpine

RUN pip install flask

COPY main.py /
EXPOSE 5000
CMD ["python3", "./main.py"]
