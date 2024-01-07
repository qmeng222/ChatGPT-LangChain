from langchain.callbacks.base import BaseCallbackHandler

# create a ChatModelStartHandler class that extends the BaseCallbackHandler:
# called when chat model starts running
class ChatModelStartHandler(BaseCallbackHandler):
    def on_chat_model_start(self, serialized, messages, **kwargs):
        print(messages)
