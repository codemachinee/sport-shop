FROM python:3.10

WORKDIR /usr/src/myapp

COPY  . /usr/src/myapp
COPY requirements_mac.txt ./
RUN pip install --no-cache-dir -r requirements_mac.txt
EXPOSE 5000
CMD [ "python", "./main.py" ]