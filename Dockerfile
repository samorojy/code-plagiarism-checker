FROM openjdk:11
WORKDIR /app

RUN apt-get update && apt-get install -y sudo python3 libpq-dev gcc python3-pip postgresql
RUN pip install psycopg2 Pygments
COPY  . .


RUN sudo service postgresql start &&  sudo -u postgres psql -U postgres -c "ALTER USER postgres PASSWORD 'postgres';" &&\
    sudo -u postgres psql -c "CREATE DATABASE index;" &&\
    sudo -u postgres psql -d index -f database.sql

EXPOSE 8080:8080

CMD ["sh", "-c", "service postgresql start && java -jar build/libs/code-plagiarism-checker-all.jar" ]