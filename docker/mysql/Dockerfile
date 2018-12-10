FROM mysql:5.7

ENV MYSQL_ROOT_PASSWORD rootpuppy
ENV MYSQL_DATABASE grafana
ENV MYSQL_USER grupo1
ENV MYSQL_PASSWORD puppybotsre.2018

ADD setup.sql /docker-entrypoint-initdb.d

EXPOSE 3306