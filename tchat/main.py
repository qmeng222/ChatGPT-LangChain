from langchain.memory import ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder, HumanMessagePromptTemplate # prompt
from langchain.chat_models import ChatOpenAI # model
from langchain.chains import LLMChain # chain
from dotenv import load_dotenv # load variables from .env


# ------ CONVERSATION BUFFER MEMORY ------
memory = ConversationBufferMemory(memory_key="messages", return_messages=True)


# ------ PROMPT ------
# prompt instance (a ChatPromptTemplate object):
prompt = ChatPromptTemplate(
  input_variables=["content", "messages"], # only 1 input var
  messages=[
    MessagesPlaceholder(variable_name="messages"),
    HumanMessagePromptTemplate.from_template("{content}")
    # {content} is a placeholder that will be filled with the value of the "content" input variable
  ]
)


# ------ MODEL ------
# load variables from a file named .env:
load_dotenv()
# load_dotenv(dotenv_path=".env2") # load variables from a file named .env2
# the .env file typically contains key-value pairs in the form of "environment variable" assignments

# model instance:
chat = ChatOpenAI()


# ------ CHAIN ------
# chain instance:
chain = LLMChain(
  memory=memory,
  prompt=prompt, # prompt
  llm=chat # model
)


while True: # infinite loop
  content = input(">> ") # input() function is used to read a line from the user
  res = chain({"content": content}) # passing a dict with keys and values (as inputs) to the chain for processing
  print(res["text"]) # for the outputs dict, a default key is "text"
# press Ctrl+C to stop the infinite loop
