FROM python:3.9-slim-buster

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt          """libraries installed in my deployment area"""

CMD ["python3", "app.py"]