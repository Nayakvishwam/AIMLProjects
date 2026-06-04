import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="dumydata",
    user="postgres",
    password="root"
)

print("Connected Successfully")

