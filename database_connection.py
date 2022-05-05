import psycopg2
from database_connection_config import config

params_ = config()

conn = psycopg2.connect(**params_)
cur = conn.cursor()
conn.autocommit = True



cur.execute("INSERT INTO Sentimentresults (orginaltweet, sentiment, subjectivity) "       
            "VALUES(%s, %s, %s)", ('test', -1, 0,)) # Deine Ergebnisse hier einfügen

cur.close()
conn.close()