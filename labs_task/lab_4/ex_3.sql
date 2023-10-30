-- Active: 1696235511511@@127.0.0.1@5432@bd_project@public

-- Подзапросы, возвращающие единичное значение

-- Запрос: Найти средний возраст мужчин в таблице Abiturient
SELECT round(AVG(age), 10) as avg_male_age
FROM (
    SELECT EXTRACT(YEAR FROM age(DateOfBirth)) AS age
    FROM Abiturient
    WHERE sex = 'm'
) AS subquery;

-- Запрос: Определить средний возраст абитуриентов, которые предоставили документы
SELECT round(AVG(EXTRACT(YEAR FROM age(DateOfBirth))), 10) as avg_age
FROM Abiturient
WHERE AbiturientID in (SELECT AbiturientID FROM Document_identifier);

-- Запрос: Найти документы самого молодого абитуриента
SELECT
    document_identifier_ID,
    Doc_type_ID,
    series_doc,
    number_doc
FROM
    Document_identifier
WHERE
    AbiturientID in (
        SELECT AbiturientID
        FROM Abiturient
        ORDER BY DateOfBirth DESC
        LIMIT 1
    )