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

exams = [
    'Математика',
    'История',
    'Биология',
    'Физика',
    'Информатика',
    'Обществознание',
    'Иностранный язык',
    'Русский язык',
    'География'
]

for exam in exams:
    cursor.execute(
            """
            INSERT INTO Exam (name_exam)
            VALUES (%s)
            """, 
        (exam,))


# Закрыть подключение
connection.commit()
cursor.close()
connection.close()
