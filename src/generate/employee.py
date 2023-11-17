import psycopg2
import sys
sys.path.append('/Users/dr0ozd/coding/bd_project/src')
from bd_info import *
import random

# Подключение к базе данных
connection = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)

cursor = connection.cursor()

male_names = [name for name in open('/Users/dr0ozd/coding/bd_project/data/names/names_m.txt', encoding='utf-8').read().strip().splitlines()]
female_names = [name for name in open('/Users/dr0ozd/coding/bd_project/data/names/names_f.txt', encoding='utf-8').read().strip().splitlines()]
male_surname = [name for name in open('/Users/dr0ozd/coding/bd_project/data/names/surname_m.txt', encoding='utf-8').read().strip().splitlines()]
female_surname = [name for name in open('/Users/dr0ozd/coding/bd_project/data/names/surname_f.txt', encoding='utf-8').read().strip().splitlines()]
male_midnames = [name for name in open('/Users/dr0ozd/coding/bd_project/data/names/midnames_m.txt', encoding='utf-8').read().strip().splitlines()]
female_midnames = [name for name in open('/Users/dr0ozd/coding/bd_project/data/names/midnames_f.txt', encoding='utf-8').read().strip().splitlines()]


for i in range(15):
    sex = random.choice(['male', 'female'])
    
    if sex == 'male':
        first_name = random.choice(male_names)
        surname = random.choice(male_surname)
        patronymic = random.choice(male_midnames)
    else:
        first_name = random.choice(female_names)
        surname = random.choice(female_surname)
        patronymic = random.choice(female_midnames)

    position = random.choices([1, 2, 3], weights=[0.2, 0.4, 0.4])[0]
    cursor.execute(
            """
            INSERT INTO Employee (first_name, surname, patronymic, PositionID)
            VALUES (%s, %s, %s, %s)
            """, 
        (first_name, surname, patronymic, position,))

# Закрыть подключение
connection.commit()
cursor.close()
connection.close()