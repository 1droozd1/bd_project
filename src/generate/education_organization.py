import psycopg2
import sys
sys.path.append('/Users/dr0ozd/coding/bd_project/src')
from bd_info import *

# Подключение к базе данных
connection = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)

cursor = connection.cursor()

with open('/Users/dr0ozd/coding/bd_project/data.txt', 'r') as f:
    schools = [line.title().strip() for line in f]
    for school in schools:
        cursor.execute("INSERT INTO Education_Organization (Name_org) VALUES (%s)", (str(school),))

# Закрыть подключение
connection.commit()
cursor.close()
connection.close()