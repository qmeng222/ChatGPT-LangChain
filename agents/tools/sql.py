# for providing lightweight, disk-based relational database:
import sqlite3

# from the langchain package > tools module, import the Tool class:
from langchain.tools import Tool

# import the BaseModel class from the Pydantic library:
from pydantic.v1 import BaseModel

from typing import List


# connect to a SQLite database (creates a new one if it doesn't exist):
conn = sqlite3.connect("db.sqlite")


# ------------ functions ------------

# list out all tables in the database:
def list_tables():
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table';") # query execution
    rows = c.fetchall() # fetch results as a list
    # print("👀", rows) # list of tuples
    # # [('users',), ('addresses',), ('products',), ('carts',), ('orders',), ('order_products',)]
    # return rows
    return "\n".join(row[0] for row in rows if row[0] is not None) # a lengthy string formatted for vertical display


def describe_tables(table_names): # a list
    c = conn.cursor() # cursor creation
    tables = ', '.join("'" + table + "'" for table in table_names)
    # tables = " 'users', 'orders', ... "
    rows = c.execute(f"SELECT sql FROM sqlite_master WHERE type='table' and name IN ({tables});") # a list of tuples
    # print("🌈", rows)
    return '\n'.join(row[0] for row in rows if row[0] is not None)


def run_sqlite_query(query):
    c = conn.cursor() # cursor creation
    try:
        c.execute(query) # query execution
        return c.fetchall() # return fetched results as a list
    except sqlite3.OperationalError as err:
        return f"The following error occured: {str(err)}"


# ------------ tools ------------

# define a new class which inherits from BaseModel:
class DescribeTablesArgsSchema(BaseModel):
    table_names: List[str] # enforce the table_names be present and be a list of string(s)

# create an instance of the Tool class based on the provided function:
describe_tables_tool = Tool.from_function(
    name="describe_tables", # name the tool
    description="Given a list of table names, returns the schema of those tables", # describe the tool
    func=describe_tables, # specify a function to execute
    args_schema=DescribeTablesArgsSchema
)

# define a new class which inherits from BaseModel:
class RunQueryArgsSchema(BaseModel):
    query: str # an instance of RunQueryArgsSchema is expected to have a query attribute of type str (enforce the query attribute be present and be a string)

# create an instance of the Tool class based on the provided function:
run_query_tool = Tool.from_function(
    name="run_sqlite_query", # name the tool
    description="Run a sqlite query.", # describe the tool
    func=run_sqlite_query, # specify a function to execute
    args_schema=RunQueryArgsSchema # if you want to use this function, you must provide an argument called query, and it's supposed to be a string
)
