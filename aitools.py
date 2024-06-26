import ollama
from types import SimpleNamespace
from system_prompt import SYSTEM_PROMPT

def _format_message(message, role='user'):
    return {
        'role': role,
        'content' : message
    }

class _AI:
    def __init__(self, model, prompt, **kwargs) -> None:
        self.model:str                  = model
        self.prompt:str                 = prompt
        self.default_response:str       = ""
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
            messages = [_format_message(self.prompt, 'system')] + message_history
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

AI = SimpleNamespace(
    summary = _AI(
        model  = "phi3",
        prompt = SYSTEM_PROMPT["SUMMARY"],
        default_response = "NO_SUMMARY",
        response_tester = lambda resp: ("Do this -" in resp)
    ),
    conversation = _AI(
        model  = "llama3",
        prompt = SYSTEM_PROMPT["CONVERSATION"],
        default_response = "Hey sorry can you elaborate a bit more?"
    ),
    function = _AI(
        model  = "mistral",
        prompt = SYSTEM_PROMPT["FUNCTION"],
        default_response = """{"tool":"conversation"}""",
        response_tester = lambda resp: resp[0] == "{" and resp[-1] == "}"
    )
)
