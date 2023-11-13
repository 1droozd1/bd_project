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

document_types = [
    'Аттестат о среднем общем образовании',
    'Диплом о среднем профессиональном образовании',
    'Диплом о высшем образовании',
    'Зарубежный диплом об образовании'
]

cursor = connection.cursor()

for doc_type in document_types:
    cursor.execute("INSERT INTO Types_Document_education (Name_doc_type) VALUES (%s)", (doc_type,))

# Закрыть подключение
connection.commit()
cursor.close()
connection.close()