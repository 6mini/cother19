import requests
import psycopg2
import logging
import sys
import json
import csv

host = "covid.cjwptwa04yyi.ap-northeast-2.rds.amazonaws.com"
port = 5432
username = "sixmini"
database = "postgres"
password = ""


def main():
    # postgreSQL 연결
    try:
        conn = psycopg2.connect(
            host=host,
            database=database,
            user=username,
            password=password)
        cursor = conn.cursor()
    except:
        logging.error("could not connect to rds")
        sys.exit()

    sql = "COPY (SELECT * FROM weather) TO STDOUT WITH CSV DELIMITER ','"
    with open("weather.csv", "w") as file:
        cursor.copy_expert(sql, file)


if __name__=='__main__':
    main()
