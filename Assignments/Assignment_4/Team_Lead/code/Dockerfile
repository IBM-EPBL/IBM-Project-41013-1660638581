FROM python:3.9
RUN apt-get update
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pip install flask
EXPOSE 5001
CMD [ "python", "app.py" ]