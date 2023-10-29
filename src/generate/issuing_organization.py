import psycopg2
import sys, csv
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

with open('/Users/dr0ozd/coding/bd_project/data/fms_unit.csv', 'r') as file:
    reader = csv.reader(file)
    organizations = [row for row in reader]

# Вставка данных в таблицу Issuing_Organization
for orgranization in organizations:
    cursor.execute("INSERT INTO Issuing_Organization (code_org, Name_org) VALUES (%s, %s)", (str(orgranization[0]).replace('-', ''), orgranization[1]))

# Закрыть подключение
connection.commit()
cursor.close()
connection.close()