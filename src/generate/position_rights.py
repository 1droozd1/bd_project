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

rights_list = {
    'admin': 'ruid',
    'manager': 'rui',
    'employee': 'r'
}

for role, value in rights_list.items():
    cursor.execute(
            """
            INSERT INTO Positions_rights (name_position, rights_position)
            VALUES (%s, %s)
            """, 
        (role, value,))
# Закрыть подключение
connection.commit()
cursor.close()
connection.close()