FROM python:3.10
WORKDIR /opt/star-burger
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY foodcartapp foodcartapp
COPY places places
COPY restaurateur restaurateur
COPY star_burger star_burger
COPY manage.py manage.py
CMD ["python3", "manage.py", "migrate"]
