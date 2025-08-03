# Stage 1: Build Stage
FROM python:3.8-slim as Build

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config

RUN pip install flask mysqlclient

COPY . .

# Stage 2: Production Stage
FROM python:3.8-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
 && rm -rf /var/lib/apt/lists/*

COPY --from=Build /app /app

COPY --from=build /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
COPY --from=build /usr/local/bin /usr/local/bin

EXPOSE 5002

CMD ["python","app.py"]