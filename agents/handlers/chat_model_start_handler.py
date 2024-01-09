from langchain.callbacks.base import BaseCallbackHandler
from pyboxen import boxen # customizable boxes in terminal

# print(
#     boxen("SAMPLE TEXT!", title="Human", color="yellow")
# )

# helper func:
def boxen_print(*args, **kwargs):
    print(boxen(*args, **kwargs))
    # a single star unpacks a sequence or collection into positional args: s = add(*values)
    # the double star unpacks a dictionary, providing values for keyword args: values = { 'a': 1, 'b': 2 }, s = add(**values)
boxen_print("SAMPLE TEXT 2!", title="Human", color="red")

# create a ChatModelStartHandler class that extends the BaseCallbackHandler:
# called when chat model starts running
class ChatModelStartHandler(BaseCallbackHandler):
    def on_chat_model_start(self, serialized, messages, **kwargs):
        # print("👀", messages) # the scratchpad/memo is a list of list [[ ... ]]

        print("\n========= 📤 Sending Messages =========\n")

        # for each record in the scratchpad/memo (a list of list):
        for message in messages[0]:
            if message.type == "system":
                boxen_print(message.content, title=message.type, color="yellow")

            elif message.type == "human":
                boxen_print(message.content, title=message.type, color="green")

            elif message.type == "ai" and "function_call" in message.additional_kwargs:
                call = message.additional_kwargs["function_call"]
                # print("👉", call) # a dict
                boxen_print(
                    f"Running tool {call['name']} with args {call['arguments']}",
                    title="ai function call",
                    color="cyan"
                )

            elif message.type == "ai":
                boxen_print(message.content, title=message.type, color="blue")

            elif message.type == "function": # result of the function call (to ChatGPT)
                boxen_print(message.content, title="res", color="purple")
                # NOTE: the write_report function in report.py doesn't actually return anything, that's why we got a final result of null
            else:
                boxen_print(message.content, title=message.type)
