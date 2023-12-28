from langchain.document_loaders import TextLoader
from dotenv import load_dotenv # load variables from .env


# ------ MODEL ------
# load variables from a file named .env:
load_dotenv()
# load_dotenv(dotenv_path=".env2") # load variables from a file named .env2


# ------ DOCUMENT LOADERS ------
loader = TextLoader("facts.txt") # an object that can load text data from the specified file path
docs = loader.load() # call the load method of the TextLoader instance ("loader")
print(docs) # [ Document(page_content='...', metadata={'source': 'facts.txt'}) ]
