from langchain.prompts import (
    ChatPromptTemplate, # create structured templates for chat interactions, specifying how the input messages are formatted or structured
    HumanMessagePromptTemplate, # for creating prompt templates that mimic human messages
    MessagesPlaceholder # for marking a placeholder within a prompt template where messages or dialogue interactions can be dynamically inserted or replaced
) # prompts

from langchain.chat_models import ChatOpenAI # model

from langchain.agents import OpenAIFunctionsAgent, AgentExecutor # an agent is a program or module that acts on behalf of a user or system to interact with OpenAI services

from dotenv import load_dotenv # load variables from .env

from tools.sql import run_query_tool # import the tool instance


# ------ MODEL ------
# load variables from the .env file:
load_dotenv()
# load_dotenv(dotenv_path=".env2") # load variables from a file named .env2

# model instance:
chat = ChatOpenAI()


# ------ PROMPT ------
# create an instance of the ChatPromptTemplate class (chat-based prompts/series of messages exchanged between user and system):
prompt = ChatPromptTemplate(
    messages=[
      HumanMessagePromptTemplate.from_template("{input}"), # human message template with a placeholder
      MessagesPlaceholder(variable_name="agent_scratchpad") # dynamically insert or replace values during the prompt generation process
    ]
)

tools = [run_query_tool] # a list of tools for future reference and utilization

agent = OpenAIFunctionsAgent(
    llm=chat,
    prompt=prompt,
    tools=tools
)

# an instance that handles the execution and coordination of agent:
agent_executor = AgentExecutor(
    agent=agent,
    verbose=True, # produce additional output or logging information during its execution
    tools=tools # specify a list of tools that the AgentExecutor can use in its execution
)

# use the agent_executor object to process the given natural language query:
agent_executor("How many users are in the database?")
