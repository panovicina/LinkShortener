FROM python:3.10.6

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt /code/requirements.txt
# Install dependencies
RUN pip install -r /code/requirements.txt
COPY entrypoint.sh .

RUN chmod +x ./entrypoint.sh

COPY . /code