from langchain.prompts import PromptTemplate # prompt
from langchain.llms import OpenAI # model
from langchain.chains import LLMChain, SequentialChain # chain
from dotenv import load_dotenv
import argparse


# load variables from a file named .env:
load_dotenv()
# the .env file typically contains key-value pairs in the form of "environment variable" assignments


# use argument parsing to avoid hard coding (provide those values as arguments when running the script from the command line)
# create an instance of the ArgumentParser class from the argparse module:
parser = argparse.ArgumentParser()

# define 2 command-line arguments with default values:
parser.add_argument("--language", default="python")
parser.add_argument("--task", default="return a list of numbers")

# arse the command-line arguments:
args = parser.parse_args()
# print("👀", args) # Namespace(language='javascript', task='print hi, qingying!')
# after parsing, the values of the arguments are stored in the args object


# prompt instances:
# 1st prompt (for code generation):
code_prompt = PromptTemplate(
  input_variables=["language", "task"],
  template="Write a very short {language} function that will {task}"
)
# 2nd prompt (for code checking/testing):
test_prompt = PromptTemplate(
  input_variables=["language", "code"],
  template="Write an unit test for the following {language} code: \n{code}"
)


# model (instance):
llm = OpenAI()


# chain instances:
# 1st chain (for code generation):
code_chain = LLMChain(
  prompt=code_prompt, # prompt
  llm=llm, # model
  output_key="code" # default key is "text"
)
# 2nd chain (for code checking/testing):
test_chain = LLMChain(
  prompt=test_prompt,
  llm=llm,
  output_key="test"
)

# connect chains:
chain = SequentialChain(
  chains=[code_chain, test_chain],
  input_variables=["language", "task"],
  output_variables=["code", "test"]
)


# input & output of the SequentialChain obje:
res = chain({
  # softcoding:
  "language": args.language,
  "task": args.task
})

print(">>>>>> RESULT:")
print(res)
# {'language': 'python', 'task': '...', 'code': '...', 'test': '...'}

print(">>>>>> GENERATED CODE:")
print(res["code"])

print(">>>>>> GENERATED TEST:")
print(res["test"])


# to run the file in terminal:
# python main.py
# python main.py --language python --task 'return a list of negative numbers'
# python main.py --language python --task 'return a list of emojis'
# python main.py --language javascript --task 'print hi, qingying!'
