FROM python:3.10
WORKDIR /opt/star-burger
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
CMD ["python3", "manage.py", "migrate"]
