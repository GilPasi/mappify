FROM public.ecr.aws/docker/library/python:3.12-slim-bookworm
WORKDIR /app

ENV MAPPIFY=/app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV SECRET_KEY=${SECRET_KEY}
ENV MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD}
ENV MYSQL_DATABASE=${MYSQL_DATABASE}
ENV MYSQL_USER=${MYSQL_USER}
ENV MYSQL_PASSWORD=${MYSQL_PASSWORD}
ENV DB_HOST=${DB_HOST}
ENV DB_ROOT_PASSWORD=${DB_ROOT_PASSWORD}

COPY /server /app/server
COPY /server/mappify_server /app/server/mappify_server
COPY ./server/ ./
COPY algorithm /app/algorithm

RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    wget \
    unzip \
    lsb-release \
    gnupg \
    ffmpeg \
    libsm6 \
    libxext6 \
    && rm -rf /var/lib/apt/lists/*


RUN pip install --upgrade pip
RUN pip install -r /app/server/requirements.txt
RUN pip install pymysql
RUN pip install matplotlib



# RUN wget "https://dev.mysql.com/get/mysql-apt-config_0.8.32-1_all.deb"
# RUN dpkg -i mysql-apt-config_0.8.32-1_all.deb

EXPOSE 8000

# CMD ["python", "mappify-server/manage.py", "runserver", "0.0.0.0:8000"]
