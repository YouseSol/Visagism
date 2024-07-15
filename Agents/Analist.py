from services.Gemini import Gemini


class Analist(Gemini):
    def __init__(self, api_key: str = ""):
        super().__init__(api_key)

        self.prompt = '''
            Act as a visagism expert. With the following characteristics extracted 
            from a photo of a person's face, create a personality profile of the 
            person based on this information: {}.

        '''
    
    def request(self, document):
        
        document = self.prompt.format(document)

        response = super().send_message(document)

        return response