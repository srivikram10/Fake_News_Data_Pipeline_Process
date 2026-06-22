import pandas as pd
import mysql.connector
import os

project_root = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

file_path = os.path.join(
    project_root,
    "data",
    "processed",
    "clean_news.csv"
)

df = pd.read_csv(file_path)

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="#ENTER_YOUR_DB_PASSWORD", #ENTER_YOUR_PASSWORD
    database="fake_news_db"
)

cursor = conn.cursor()

for _, row in df.iterrows():

    sql = """
    INSERT INTO news_data
    (title,text,subject,date,label)
    VALUES (%s,%s,%s,%s,%s)
    """

    values = (
        row["title"],
        row["text"],
        row["subject"],
        row["date"],
        row["label"]
    )

    cursor.execute(sql, values)

conn.commit()

print("Data Loaded Successfully!")

cursor.close()
conn.close()