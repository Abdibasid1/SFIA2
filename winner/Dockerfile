FROM python:latest
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5003
ENTRYPOINT ["python3", "app.py"]