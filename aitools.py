import ollama
from types import SimpleNamespace

def _format_message(message, role='user'):
    return {
        'role': role,
        'content' : message
    }

class _AI:
    def __init__(self, model, prompt, json_response=False, **kwargs) -> None:
        self.model:str                  = model
        self.prompt:str                 = prompt
        self.default_response:str       = ""
        self.json_response:bool         = json_response
        self.response_tester:function   = lambda x: True
        
        for arg, value in kwargs.items():
            if arg == "default_response":
                self.default_response = value
            elif arg == "response_tester":
                self.response_tester = value
        
    def chat(self, message_history:list):
        '''Send a message history to llm and recieve response'''
        
        message_history = list(filter(lambda x: x['role']!='system', message_history))
        
        assistant_response = ollama.chat(
            model    = self.model,
            messages = [_format_message(self.prompt, 'system')] + message_history,
            format   = 'json' if self.json_response else '',
        )['message']['content'].strip()
        
        try:
            if not self.response_tester(assistant_response):
                assistant_response = self.default_response
        except Exception as e:
            print("CANNOT TEST :", e)
            assistant_response = self.default_response
            
        return assistant_response

    def simple_chat(self, message:str):
        '''Send a single message to llm, and recieve response.'''
        
        return self.chat([_format_message(message)])

class _Request:
    VALID_TYPES = ["CONVERSATION", "FUNCTION"]
    def __init__(self, type_="CONVERSATION", data_="") -> None:
        if type_ not in _Request.VALID_TYPES:
            type_ = "CONVERSATION"
        self.type_ = type_
        self.data_ = data_
        
