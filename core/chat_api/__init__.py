import requests
from core.chat_api.provedores import *

provedores_suportados = {
    OpenAI.placeholer(): {
        "modelos": OpenAI.modelos(),
        "api_url": "https://api.openai.com/v1/chat/completions"
    },
    Gemini.placeholer(): {
        "modelos": Gemini.modelos(),
        "api_url": "https://generativelanguage.googleapis.com/v1beta/models"
    },
    DeepSeek.placeholer(): {
        "modelos": DeepSeek.modelos(),
        "api_url": "https://api.deepseek.com/chat/completions"
    }
}

class ChatAPI:
    def __init__(self, provedor="", modelo="", api_key=""):
        print("chat iniciado com o provedor", provedor)
        if(provedor not in provedores_suportados.keys()):
            raise UnsupportedProviderError(provedor)

        if(modelo not in provedores_suportados[provedor]["modelos"]):
            raise UnsupportedProviderModelError(provedor, modelo)

        self.provedor = provedor
        self.api_url = provedores_suportados[provedor]["api_url"]
        self.modelo = modelo
        self.api_key = api_key

    
    def ajusta_retorno(self, conteudo):
        if("```json" in conteudo):
            return conteudo.replace("```json", "").replace("```", "")

    def gera_conteudo(self, contexto, prompt):
        url = self.api_url
        headers = {
            "Content-Type": "application/json"
        }

        payload = {}

        if(self.provedor == "gemini"):
            url = f'{self.api_url}/{self.modelo}:generateContent?key={self.api_key}'
            payload = {
                "contents": [
                    {
                        "role": "model",
                        "parts": [{"text": contexto}]
                    },
                    {
                        "role": "user",
                        "parts": [{"text": prompt}]
                    }
                ]
            }
        else:
            headers["Authorization"] = f'Bearer {self.api_key}'
            payload = {
                "model": self.modelo,
                "messages": [
                    {"role": "system", "content": contexto},
                    {"role": "user", "content": prompt},
                ]
            }

        resp = requests.post(url, headers=headers, json=payload)

        if(resp.status_code == 200):
            data = resp.json()
            if(self.provedor == "gemini"):
                candidates = data["candidates"]
                content = candidates[0]["content"]
                parts = content["parts"][0]
                return self.ajusta_retorno(parts["text"])
            else:
                choices = data["choices"][0]
                message = choices["message"]
                content = message["content"]
                return self.ajusta_retorno(content)

        elif(resp.status_code == 400):
            print(resp.text)
        elif(resp.status_code == 401):
            print(resp.text)
        else:
            print(resp.url)
            print(resp.status_code)
            print(resp.text)