from langchain.prompts import PromptTemplate # prompt
from langchain.llms import OpenAI # model
from langchain.chains import LLMChain # chain
from dotenv import load_dotenv
import argparse


# load variables from a file named .env:
load_dotenv()
# the .env file typically contains key-value pairs in the form of "environment variable" assignments


# use argument parsing to avoid hard coding (provide those values as arguments when running the script from the command line)
# create an instance of the ArgumentParser class from the argparse module:
parser = argparse.ArgumentParser()

# define a command-line arguments with default values:
parser.add_argument("--language", default="python")
parser.add_argument("--task", default="return a list of numbers")

# arse the command-line arguments:
args = parser.parse_args()
# print("👀", args) # Namespace(language='javascript', task='print hi, qingying!')
# after parsing, the values of the arguments are stored in the args object


# prompt (instance):
code_prompt = PromptTemplate(
  input_variables=["language", "task"],
  template="Write a very short {language} function that will {task}"
)


# model (instance):
# SECURE THIS KEY!
llm = OpenAI()


# chain (instance):
code_chain = LLMChain(
  prompt=code_prompt, # prompt
  llm=llm # model
)


# input & output:
res = code_chain({
    "language": args.language,
    "task": args.task
})
print(res["text"])


# to run the file in terminal:
# python main.py
# python main.py --language javascript --task 'print hi, qingying!'
