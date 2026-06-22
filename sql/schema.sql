CREATE DATABASE fake_news_db;

USE fake_news_db;

CREATE TABLE news_data(
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(500),
    text LONGTEXT,
    subject VARCHAR(100),
    date DATE,
    label INT
);