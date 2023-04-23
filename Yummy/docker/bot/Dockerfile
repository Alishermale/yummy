FROM python:3.9
WORKDIR .
COPY ../../. .
COPY ../../app/main.py .
COPY docker/bot/configs/requirements.txt .
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
CMD python main.py
