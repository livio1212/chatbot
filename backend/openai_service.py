import openai
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))



def get_openai_response(message):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": (
                    "Voce é um amigo empatico e acolhedor"
                    "seu papel é ouver e consolar pessoas que se encontram tristes ou em busca de companhia"
                    "Evite responder perguntas tecnicas fora do tema emocional, foque sempre na empatia e na escuta ativa"
                    "caso identifique algum quadro de depressao ou outra doenca psicologica comportamental aconcelhe a buscar um profissional, em casos urgentes como pensamentos suicidas aconcelhe o usuario a consultar o 188 numero do centro de valorizaçao da vida"
                )
            },
            {
                "role": "user",
                "content": message
            }
        ]
    )
    return response.choices[0].message.content.strip()
