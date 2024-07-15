from services.Gemini import Gemini


class CutAnalist(Gemini):
    def __init__(self, api_key: str = ""):
        super().__init__(api_key)

        self.prompt = '''
            Act as a visagism and hairdressing specialist. Use the following 
            descriptions of a male face to provide ideas for ideal cuts for 
            him using visagism techniques: {}.

        '''
    
    def request(self, document):
        
        document = self.prompt.format(document)

        response = super().send_message(document)

        return response