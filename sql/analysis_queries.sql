-- Fake vs Real News Count
SELECT label, COUNT(*) AS total
FROM news_data
GROUP BY label;

-- News by Subject
SELECT subject, COUNT(*) AS total
FROM news_data
GROUP BY subject
ORDER BY total DESC;

-- Top 10 Subjects
SELECT subject, COUNT(*) AS total
FROM news_data
GROUP BY subject
ORDER BY total DESC
LIMIT 10;