import time
import google.generativeai as genai

class gemini:

    def __init__(self, API_KEY):
        self.API_KEY = API_KEY
        self.client = genai.GenerativeModel("gemini-1.5-flash")

    

