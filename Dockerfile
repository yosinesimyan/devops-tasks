#start by pulling the python docker image

FROM python:3.8-alpine

#copy the files required to the image

COPY ./requirements.txt /app/requirements.txt
COPY ./tasks.py /app/tasks.py
COPY ./tasks_db.py /app/tasks_db.py
COPY ./json_files.py /app/json_files.py
COPY ./tasks.json /app/tasks.json

#switch working dir

WORKDIR /app

#install the dipendencies and packages in the requirements file
RUN pip install -r requirements.txt

#configure the container to run in an executed manner

ENTRYPOINT ["python"]

CMD ["tasks.py"]
