from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import mysql.connector
import os

# Load environment variables
load_dotenv()

# Get DB credentials from .env
DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT"))
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

# FastAPI app
app = FastAPI()

# Database connection
conn = mysql.connector.connect(
    host=DB_HOST,
    port=DB_PORT,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)
cursor=conn.cursor(dictionary=True)

class Skill(BaseModel):
    skill_name: str
    topics: str
    skill_level: str
    goal: str
    completion_date: str
@app.post("/skills")
def add_skill(skill:Skill):
    query="""
    INSERT INTO skills(skill_name,topics,skill_level,goal,completion_date)
    VALUES(%s,%s,%s,%s,%s)
    """
    values=(
        skill.skill_name,
        skill.topics,
        skill.skill_level,
        skill.goal,
        skill.completion_date
    )
    cursor.execute(query,values)
    conn.commit()
    return{"message":"Skill Added"}

@app.get("/view_skills")
def view_skills():
    query="SELECT * FROM skills"
    cursor.execute(query)
    result=cursor.fetchall()
    return result

@app.put("/update_skill/{skill_id}")

def update_skill(skill_id: int, skill: Skill):
    query="""
    UPDATE skills
    SET skill_name=%s, topics=%s, skill_level=%s, goal=%s, completion_date=%s
    WHERE skill_id=%s
    """
    values=(
        skill.skill_name,
        skill.topics,
        skill.skill_level,
        skill.goal,
        skill.completion_date,
        skill_id
    )
    cursor.execute(query,values)
    conn.commit()
    return{"message":"Skill Updated"}
