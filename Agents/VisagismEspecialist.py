from services.GeminiProVision import GeminiProVision

class VisagismEspecialist(GeminiProVision):
    def __init__(self, api_key=""):
        super().__init__(api_key)
        
        self.prompt = '''
            Answer the following questions about the image of this person's face:

            Perguntas sobre Formato de Rosto
                Qual é o formato do rosto (oval, redondo, quadrado, coração, diamante, etc.)?
                A largura da testa é maior, menor ou igual à largura da mandíbula?
                O comprimento do rosto é maior, menor ou igual à largura do rosto?

            Perguntas sobre Cores
                Qual é a cor predominante dos olhos?
                Qual é a cor predominante do cabelo?
                Qual é o tom de pele da pessoa (frio, quente, neutro)?

            Perguntas sobre Principais Linhas da Face
                Quais são as linhas faciais mais pronunciadas (linhas do sorriso, linhas da testa, etc.)?
                A pessoa tem covinhas ou outras marcas características no rosto?
                As maçãs do rosto são proeminentes ou discretas?
                Perguntas sobre Formato do Nariz
                O nariz é reto, aquilino, arrebitado, ou outro formato?
                A largura do nariz é estreita, média ou larga?
                A ponta do nariz é arredondada, pontiaguda ou achatada?
                
            Perguntas sobre Formato da Orelha
                As orelhas são pequenas, médias ou grandes em relação ao rosto?
                As orelhas são coladas à cabeça ou mais afastadas?
                Qual é o formato do lóbulo da orelha (preso, solto)?
                
            Perguntas sobre Formato dos Olhos
                Os olhos são amendoados, redondos, ou outro formato?
                A distância entre os olhos é pequena, média ou grande?
                As pálpebras são visíveis ou escondidas?
                
            Perguntas sobre Formato da Boca
                Os lábios são finos, médios ou cheios?
                O lábio superior é mais proeminente, igual ou menos proeminente que o lábio inferior?
                A boca é larga, média ou estreita?
                
            Perguntas sobre Formato do Queixo e Maxilar
                O queixo é pontiagudo, arredondado ou quadrado?
                A mandíbula é larga, média ou estreita?
                O queixo é recuado, alinhado ou proeminente?
                
            Perguntas sobre Formato da Testa
                A testa é alta, média ou baixa?
                A linha do cabelo é reta, arredondada, em V ou em outro formato?
                A testa é larga, média ou estreita?

        '''

    def request(self, image):

        response = super().send_message(self.prompt, image)

        return response