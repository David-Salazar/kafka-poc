# %%
import pymysql


ENDPOINT = "database-kaka.c8wdpocz3thc.us-east-1.rds.amazonaws.com"
PASSWORD = "Bf2TiD4M4aOpbglEd9lM"
DBNAME = "databasekafka"
USR = "admin"
PORT = 3306
connection = pymysql.connect(host=ENDPOINT, user=USR, password=PASSWORD, port=PORT, db=DBNAME)

with connection.cursor() as cur:
    cur.execute('SELECT * FROM covid_tweets')

    rows = cur.fetchall()
    print(rows)
    for row in rows:
        print(f'{row[0]} {row[1]} {row[2]}')
