# for providing lightweight, disk-based relational database:
import sqlite3

# from the langchain package > tools module, import the Tool class:
from langchain.tools import Tool


# connect to a SQLite database (creates a new one if it doesn't exist):
conn = sqlite3.connect("db.sqlite")


def run_sqlite_query(query):
    c = conn.cursor() # cursor creation
    c.execute(query) # query execution
    return c.fetchall() # return the fetched results as a list


# create an instance of the Tool class based on the provided function:
run_query_tool = Tool.from_function(
    name="run_sqlite_query", # name the tool
    description="Run a sqlite query.", # describe the tool
    func=run_sqlite_query # specify a function to execute
)
