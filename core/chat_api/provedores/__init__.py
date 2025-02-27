

class Gemini:
    def __init__(self, API_KEY=""):
        ...

    @staticmethod
    def placeholer():
        return "gemini"

    @staticmethod
    def modelos():
        # https://ai.google.dev/gemini-api/docs/models/gemini?hl=pt-br
        return ["gemini-2.0-flash", "gemini-2.0-flash-lite", "gemini-1.5-flash", "gemini-1.5-flash-8b", "gemini-1.5-pro"]

class OpenAI:
    def __init__(self, API_KEY=""):
        ...

    @staticmethod
    def placeholer():
        return "openai"

    @staticmethod
    def modelos():
        # https://platform.openai.com/docs/models#models-overview
        return ["gpt-4o", "gpt-4o-mini", "o1", "o3-mini", "gpt-4-turbo", "gpt-3.5-turbo"]

class DeepSeek:
    def __init__(self, API_KEY=""):
        ...

    @staticmethod
    def placeholer():
        return "deepseek"

    @staticmethod
    def modelos():
        # https://api-docs.deepseek.com/quick_start/pricing
        return ["deepseek-chat"]

class UnsupportedProviderError(Exception):
    """
        -
    """
    def __init__(self, provider, message="Provedor não suportado ou não implementado."):
        self.provider = provider
        self.message = f"{message} Provedor fornecido: '{provider}'."
        super().__init__(self.message)

class UnsupportedProviderModelError(Exception):
    """
        -
    """
    def __init__(self, provider, model, message="Modelo não suportado ou não implementado"):
        self.provider = provider
        self.model = model
        self.message = f"{message} O modelo '{model}' não está disponível para o provedor '{provider}'"
        super().__init__(self.message)