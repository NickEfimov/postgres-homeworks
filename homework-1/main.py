"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv


conn = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password='12345'
)

cur = conn.cursor()

with open('north_data/employees_data.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", row)

with open('north_data/customers_data.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        cur.execute("INSERT INTO costumers VALUES (%s, %s, %s)", row)

with open('north_data/orders_data.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", row)


conn.commit()
cur.close()
conn.close()
