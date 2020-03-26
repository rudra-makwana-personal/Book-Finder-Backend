FROM python:3
#RUN apk --update add bash nano
#ENV STATIC_URL /static
#ENV STATIC_PATH /var/www/app/static
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python3","notesShowAdd.py"]