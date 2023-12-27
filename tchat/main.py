from langchain.memory import ConversationBufferMemory, ConversationSummaryMemory, FileChatMessageHistory
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder, HumanMessagePromptTemplate # prompt
from langchain.chat_models import ChatOpenAI # model
from langchain.chains import LLMChain # chain
from dotenv import load_dotenv # load variables from .env


# ------ MODEL ------
# load variables from a file named .env:
load_dotenv()
# load_dotenv(dotenv_path=".env2") # load variables from a file named .env2
# the .env file typically contains key-value pairs in the form of "environment variable" assignments

# model instance:
chat = ChatOpenAI(verbose=True)


# ------ MEMORY ------
# ref: https://python.langchain.com/docs/modules/memory/types/summary
# memory = ConversationBufferMemory(
memory = ConversationSummaryMemory(
  # chat_memory=FileChatMessageHistory("history.json"), # store chat history in `history.json` file
  llm=chat,
  memory_key="messages",
  return_messages=True
)


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


# ------ CHAIN ------
# chain instance:
chain = LLMChain(
  memory=memory,
  prompt=prompt, # prompt
  llm=chat, # model
  verbose=True
)


while True: # infinite loop
  content = input(">> ") # input() function is used to read a line from the user
  res = chain({"content": content}) # passing a dict with keys and values (as inputs) to the chain for processing
  print(res["text"]) # for the outputs dict, a default key is "text"
# press Ctrl+C to stop the infinite loop
