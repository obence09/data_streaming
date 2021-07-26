#Ingesting Data
'''Pulling the data and processing it'''

import requests
import psycopg2


#you have to give your own credentials at user and password
conn = psycopg2.connect(dbname = "test_python", user="postgres", password = "postgres")
cur = conn.cursor()
sql = "INSERT INTO transactions (txid, uid, amount) VALUES (%s, %s, %s)"

#streaming 10 rows of data from API to postgresql database
with requests.get("http://127.0.0.1:5000/very_large_request/10", stream=True) as request:
    buffer = ""
    for chunk in request.iter_content(chunk_size=1):
        if chunk.endswith(b'\n'):
            t = eval(buffer)
            cur.execute(sql, (t[0], t[1],t[2]))
            conn.commit( )
            buffer=""
        else:
            buffer += chunk.decode()
