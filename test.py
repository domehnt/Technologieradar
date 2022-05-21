
import psycopg2
from database_connection_config import config

def get_digitsentimentresults() :

    params_ = config()
    conn = psycopg2.connect(**params_)

    cur = conn.cursor()
    conn.autocommit = True

    resultDigits = []
    cur.execute("select sentiment from sentimentresults order by sentiment;")

    while True:
        try:
            row = cur.fetchone()
            data = float(row[0])
            resultDigits.append(data)

        except TypeError :
            break
    cur.close()
    conn.close()
    return resultDigits

print(get_digitsentimentresults())