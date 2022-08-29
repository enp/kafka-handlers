FROM python:latest
RUN pip install aiokafka
WORKDIR /app
COPY app/*.py /app/
USER 1001:1001
CMD python /app/consumer.py
