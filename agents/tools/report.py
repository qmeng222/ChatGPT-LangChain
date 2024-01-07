from langchain.tools import StructuredTool # for taking in multiple inputs of arbitrary types
from pydantic.v1 import BaseModel # for defining a model and data validation


# define a Python class for data validation:
class WriteReportArgsSchema(BaseModel):
    filename: str
    html: str

# write HTML content to a file:
def write_report(filename, html):
    with open(filename, 'w') as f: # open the file in write mode (the with block ensures the file is properly closed after the write operation is completed, even if an error occurs during the writing process)
        f.write(html) # write the provided HTML content (html parameter) to the opened file (f)

# NOTE: the Tool class can only use functions that receive a single argument; to make a tool that's going to receive multiple arguments, use StructuredTool class instead:
write_report_tool = StructuredTool.from_function(
    name="write_report", # name the tool
    description="Write an HTML file to disk. Use this tool whenever someone asks for a report.", # describe the tool
    func=write_report, # specify a function to execute
    args_schema=WriteReportArgsSchema # specify the argument schema (the expected structures and types of inputs for a function)
)
