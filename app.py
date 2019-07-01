from flask import Flask
import psycopg2
from psycopg2 import pool
import os

DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]
DB_USER = os.environ["DB_USER"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_DATABASE = os.environ["DB_DATABASE"]

app = Flask(__name__)


conn_pool = psycopg2.pool.ThreadedConnectionPool(
    1,
    2,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT,
    database=DB_DATABASE,
)


@app.route("/hello")
def hello():
    try:
        conn = conn_pool.getconn()
        cursor = conn.cursor()
        cursor.execute("select * from foo")
        recs = cursor.fetchall()
        s = ""
        for row in recs:
            s += str(row)
        cursor.close()
        return "Hello, World! " + s
    finally:
        if conn and conn_pool:
            conn_pool.putconn(conn)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
