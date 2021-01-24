# %%
import pymysql
import logging

def create_database():
    """Creates a database"""
    connection = pymysql.connect(host=ENDPOINT, user=USR, password=PASSWORD, port=PORT,
                                 cursorclass= pymysql.cursors.DictCursor,
                                 charset="utf8mb4")
    with connection.cursor() as cursor:
        sql = "CREATE DATABASE IF NOT EXISTS databasekafka;"
        cursor.execute(sql)
    connection.commit()
    connection.close()


def create_table():
    """Create table in the database"""
    connection = pymysql.connect(host=ENDPOINT, user=USR, password=PASSWORD, port=PORT, db=DBNAME)
    sql = """CREATE TABLE IF NOT EXISTS covid_tweets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tweet VARCHAR(512),
    date_creation DATETIME,
    sentiment_prediction VARCHAR(512),
    sentiment_score NUMERIC,
    topic_prediction VARCHAR(512),
    topic_score NUMERIC);"""
    with connection.cursor() as cursor:
        cursor.execute("DROP TABLE IF EXISTS covid_tweets")
        logging.info("Drop table")
        cursor.execute(sql)
        logging.info("Created table")
    connection.commit()
    connection.close()


if __name__ == "__main__":
    ENDPOINT = "database-kaka.c8wdpocz3thc.us-east-1.rds.amazonaws.com"
    PASSWORD = "Bf2TiD4M4aOpbglEd9lM"
    DBNAME = "databasekafka"
    USR = "admin"
    PORT = 3306
    create_database()
    create_table()
