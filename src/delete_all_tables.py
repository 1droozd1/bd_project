'''Модуль удаления всех таблиц со всей информацией'''
import psycopg2
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

# Получение списка всех таблиц
cursor.execute("""
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema = 'public'
""")
tables = cursor.fetchall()

# Удаление каждой таблицы
for table in tables:
    cursor.execute(f"DROP TABLE IF EXISTS {table[0]} CASCADE")
    print(f"Таблица {table[0]} удалена.")

# Закрыть подключение
connection.commit()
cursor.close()
connection.close()
