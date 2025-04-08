from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
import os
import sqlite3
import re

#load all envs
load_dotenv()

#configure api key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#load gemini model
def get_gemini_response(question,prompt):
    model=genai.GenerativeModel("gemini-1.5-pro")
    response=model.generate_content([prompt[0],question])
    return response.text

#function to retrieve query from sql db
def read_sql_query(sql,db):
    sql = re.sub(r"```(?:sql)?\s*([\s\S]*?)\s*```", r"\1", sql).strip()

    conn=sqlite3.connect(db)
    cursor=conn.cursor()
    cursor.execute(sql)
    rows=cursor.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME,CLASS,SECTION and 
    MARKS. For example, Example 1 - How many entries of records are present, the SQL command would be something like this
    SELECT COUNT(*) FROM STUDENT;\nExample 2 - Tell me all the students studying in the data science class?,
    the SQL command would be like this, SELECT * FROM STUDENT where CLASS="Data Science"
    """
]

st.set_page_config(page_title="I can retrieve any SQL query")
question=st.text_input("Input: ",key="input")
submit=st.button("Ask Qn")

if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    data=read_sql_query(response,"student.db")
    st.subheader("The response is:")
    for row in data:
        print(row)
        st.header(row)