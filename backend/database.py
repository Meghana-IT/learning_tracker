from dotenv import load_dotenv
import mysql.connector
import os

# Load env variables
load_dotenv()

# Database connection
conn = mysql.connector.connect(
    host=os.getenv("DB_HOST").strip(),
    port=int(os.getenv("DB_PORT")),
    user=os.getenv("DB_USER").strip(),
    password=os.getenv("DB_PASSWORD").strip(),
    database=os.getenv("DB_NAME").strip(),
    ssl_disabled=False
)

cursor = conn.cursor(dictionary=True)

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS skills (
    skill_id INT AUTO_INCREMENT PRIMARY KEY,
    skill_name VARCHAR(255),
    topics TEXT,
    skill_level VARCHAR(255),
    goal TEXT,
    completion_date DATE
)
""")

conn.commit()