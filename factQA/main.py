from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv # load variables from .env


# load variables from a file named .env:
load_dotenv()
# load_dotenv(dotenv_path=".env2") # load variables from a file named .env2


# ------ TEXT SPLITTER ------
text_splitter = CharacterTextSplitter(
  separator="\n",
  chunk_size=200, # each chunk of text will contain at most 200 characters
  chunk_overlap=0 # number of chars by which consecutive chunks can overlap (no overlap between chunks)
  # chunk_overlap=100 # play with this parameter & see how it works
)


# --- EMBEDDINGS (for each chunk) ---
embeddings = OpenAIEmbeddings()

# # run a quick test:
# emb = embeddings.embed_query("I like cooking.")
# print(emb) # a list of numbers

# ------ DOCUMENT LOADERS ------
# load text data from the specified file path:
loader = TextLoader("facts.txt")

# call the load_and_split method of the TextLoader instance ("loader"):
docs = loader.load_and_split(
    text_splitter=text_splitter
)

# print(docs)
# # list of sub documents:
# [ Document(page_content="1. ...\n2. ...\n3. ...", metadata={'source': 'facts.txt'}),
#   Document(page_content="4. ...\n5. ...",         metadata={'source': 'facts.txt'}),
#   ... ]

# print("---------")
# for doc in docs:
#   print(doc.page_content, "\n")
