from langchain.prompts import (
    ChatPromptTemplate, # create structured templates for chat interactions, specifying how the input messages are formatted or structured
    HumanMessagePromptTemplate, # for creating prompt templates that mimic human messages
    MessagesPlaceholder # for marking a placeholder within a prompt template where messages or dialogue interactions can be dynamically inserted or replaced
) # prompts

from langchain.chat_models import ChatOpenAI # model

from langchain.schema import SystemMessage

from langchain.agents import OpenAIFunctionsAgent, AgentExecutor # an agent (pretty much a chain) is a module that acts on behalf of a user or system to interact with OpenAI services

from dotenv import load_dotenv # load variables from .env

from tools.sql import run_query_tool, list_tables # import funcs from tools/sql.py


# ------ MODEL ------
# load variables from the .env file:
load_dotenv()
# load_dotenv(dotenv_path=".env2") # load variables from a file named .env2

# model instance:
chat = ChatOpenAI()


# ------ PROMPT ------

# (sys msg) list out all tables in the db:
tables = list_tables()
# print(tables) # [('users',), ('addresses',), ('products',), ('carts',), ('orders',), ('order_products',)] -> 'users\naddresses\n...'

# create an instance of the ChatPromptTemplate class (chat-based prompts/series of messages exchanged between user and system):
prompt = ChatPromptTemplate(
    messages=[
      SystemMessage(content=f"You are an AI that has access to a SQLite database.\n{tables}"), # system message about tables in the database
      HumanMessagePromptTemplate.from_template("{input}"), # human message template with a placeholder
      MessagesPlaceholder(variable_name="agent_scratchpad") # dynamically insert or replace values during the prompt generation process & think of that agent_scratchpad as being like a form of memory (for tracking human msgs, assistant msgs, and function msgs) inside our app
    ]
)

tools = [run_query_tool] # a list of tools for future reference and utilization

# an agent takes a list of tools & convert them into JSON function descriptions:
agent = OpenAIFunctionsAgent(
    llm=chat,
    prompt=prompt,
    tools=tools
)

# an agent executor takes an agent (pretty much a chain) & runs that chain over and over again until the response we get back from ChatGPT is not a function call (essentially a fancy while loop):
agent_executor = AgentExecutor(
    agent=agent,
    verbose=True, # produce additional output or logging information during its execution
    tools=tools # specify a list of tools that the AgentExecutor can use in its execution
)

# use the agent_executor object to process the given natural language query:
# agent_executor("How many users are in the database?")
agent_executor("How many users have provided a shipping address?")

