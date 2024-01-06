# for providing lightweight, disk-based relational database:
import sqlite3

# from the langchain package > tools module, import the Tool class:
from langchain.tools import Tool


# connect to a SQLite database (creates a new one if it doesn't exist):
conn = sqlite3.connect("db.sqlite")


# list out all tables in the database:
def list_tables():
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table';") # query execution
    rows = c.fetchall() # fetch results as a list
    # print("👀", rows) # list of tuples
    # # [('users',), ('addresses',), ('products',), ('carts',), ('orders',), ('order_products',)]
    # return rows
    return "\n".join(row[0] for row in rows if row[0] is not None) # a lengthy string formatted for vertical display


def run_sqlite_query(query):
    c = conn.cursor() # cursor creation
    try:
        c.execute(query) # query execution
        return c.fetchall() # return fetched results as a list
    except sqlite3.OperationalError as err:
        return f"The following error occured: {str(err)}"


# create an instance of the Tool class based on the provided function:
run_query_tool = Tool.from_function(
    name="run_sqlite_query", # name the tool
    description="Run a sqlite query.", # describe the tool
    func=run_sqlite_query # specify a function to execute
)
