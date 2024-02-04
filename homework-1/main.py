"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2


conn = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password='12345'
)

cur = conn.cursor()

f = open('north_data/employees_data.csv', 'r', encoding='utf8')
data = f.readlines()
rows = []
for row in data[1:]:
    line_tuple = tuple(row.strip(',').split('","'))
    rows.append(line_tuple)
    final = (rows[-1:])
    print(final)
    #cur.executemany("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", final)


#conn.commit()

#cur.close()
#conn.close()
