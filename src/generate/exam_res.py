import psycopg2
import sys, csv
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

cursor.execute("SELECT COUNT(AbiturientID) FROM Abiturient")
count_abitur = int(cursor.fetchall()[0][0])

cursor.execute("""
    SELECT 
        A.AbiturientID,
        E.ExamID 
    FROM 
        Abiturient A
    JOIN 
        Application_for_admission AA ON A.AbiturientID = AA.AbiturientID
    JOIN 
        Programm_for_study PS ON AA.SpecialityID = PS.ProgrammID
    JOIN 
        Exam E ON PS.ExamID = E.ExamID;

""")

dict_abitur = {}
for student in cursor.fetchall():
    try:
        dict_abitur[student[0]].append(student[1])
    except KeyError:
        dict_abitur[student[0]] = [student[1]]

for id in range(1, count_abitur + 1):
    for exam in dict_abitur[id]:
        cursor.execute(
                """
                INSERT INTO Exam_res (AbiturientID, ExamID, score)
                VALUES (%s, %s, %s)
                """, 
            (id, exam, random.randint(50, 100),))

# Закрыть подключение
connection.commit()
cursor.close()
connection.close()