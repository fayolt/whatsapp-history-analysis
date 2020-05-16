FROM python:3.6-slim-buster
RUN mkdir /app
WORKDIR /app
COPY ./requirements.txt /app
RUN pip install -r requirements.txt
COPY . /app
CMD [ "python", "-m", "history_analysis" ]