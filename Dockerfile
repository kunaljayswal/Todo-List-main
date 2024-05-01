FROM python:3.10
FROM tiangolo/uwsgi-nginx:python3.9


WORKDIR /data

RUN apt-get update && apt-get install -y --no-install-recommends gcc

COPY . .

COPY ./requirements.txt /api
# Install production dependencies
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

Run python manage.py makemigrations
RUN python manage.py migrate

EXPOSE 8000

CMD ["python","manage.py","runserver","0.0.0.0:8000"]
