import psycopg2
import sys
sys.path.append('/Users/dr0ozd/coding/bd_project/src')
from bd_info import *

# Массив значений для вставки
document_types = [
    'Паспорт РФ',
    'Свидетельство о рождении',
    'Паспорт иностранного гражданина',
    'Временное удостоверение личности',
    'Загранпаспорт',
    'Вид на жительство'
]

# Подключение к базе данных
connection = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)

cursor = connection.cursor()

# Вставка данных в таблицу Types_Document_identifier
for doc_type in document_types:
    cursor.execute("INSERT INTO Types_Document_identifier (Name_doc_type) VALUES (%s)", (doc_type,))

# Закрыть подключение
connection.commit()
cursor.close()
connection.close()
