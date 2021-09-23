FROM python:3.9.2

WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/app/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./exchangerates/ /usr/src/app/
COPY exchangerates/.env /usr/src/app/.env

#COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
#RUN chmod +x /usr/src/app/entrypoint.sh
#ENTRYPOINT ["/usr/src/app/entrypoint.sh"]