# Define environment variable
# ENV NAME World

FROM public.ecr.aws/docker/library/python:3.12-slim-bookworm
WORKDIR /app
COPY mappify-server /app/mappify-server
COPY algorithm /app/algorithm

RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    wget \
    unzip \
    lsb-release \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install -r mappify-server/requirements.txt

RUN wget "https://dev.mysql.com/get/mysql-apt-config_0.8.32-1_all.deb"
RUN dpkg -i mysql-apt-config_0.8.32-1_all.deb

EXPOSE 8000
CMD ["ls", "mysql-apt-config_0.8.32-1_all.deb"]
# CMD ["python", "mappify-server/manage.py", "runserver", "0.0.0.0:8000"]
