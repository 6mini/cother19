import requests
import psycopg2
import logging
import sys
import json
import csv

key = ''
startDate = '20201005'
endDate = '20211005'
location = '108' # 서울

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

    # cursor.execute("""CREATE TABLE confirmed (
    #     date VARCHAR PRIMARY KEY NOT NULL,
    #     confirmed INT,
    #     FOREIGN KEY(date) REFERENCES weather(date))
    # """)
    # conn.commit()
    # sys.exit()

    with open('covid-confirmed-in-seoul.csv') as f:
        raw = csv.reader(f)
        for row in raw:
            confirmed = {}
            confirmed.update(
                {
                    'date': row[0],
                    'confirmed': row[1]
                }
            )
            insert_row(cursor, confirmed, 'confirmed')
    conn.commit()


def insert_row(cursor, data, table):
    
    placeholders = ', '.join(['%s'] * len(data))
    columns = ', '.join(data.keys())
    key_placeholders = ', '.join(['{0}=%s'.format(k) for k in data.keys()])
    sql = "INSERT INTO %s ( %s ) VALUES ( %s ) ON CONFLICT ( %s ) DO UPDATE SET  %s" % (table, columns, placeholders, list(data.keys())[0] ,key_placeholders)
    cursor.execute(sql, list(data.values())*2)


if __name__=='__main__':
    main()