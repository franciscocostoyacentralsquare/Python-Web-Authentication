import psycopg2
from config import config
import json
import decryptor

def connect(us,pw):
    """ Connect to the PostgreSQL database server """
    conn = None
    us = us
    pw = pw
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

   # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')
        #cur.execute(f"SELECT EXISTS(SELECT * FROM username WHERE username={us}  AND password={pw});")

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

       # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')



def pwcheck(data):
    data = json.loads(data)
    us = data.get("username")
    pw = data.get("password")
    print("username: ",us,"password: ",pw)
    connect(us,pw)
