FROM python:3

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

ENV CHROME_DRIVER_PATH=chrome_driver_path

CMD ["python", "main.py"]
