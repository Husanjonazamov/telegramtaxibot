FROM python:3.11-slim

WORKDIR /usr/src/app

RUN pip install --upgrade pip

COPY . .

RUN pip install -r requirements.txt

CMD ["python3", "bot.py"]
