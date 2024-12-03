"""
api.py

Description: 
    Handles gemini api and provides a method to query the api
"""


import time #for when i implement rate limiting or something
import google.generativeai as genai

class gemini:
    """
    Manages the gemini api
    """
    
    PROMPT = "Is {} odd? Respond with 'yes' or 'no' only."

    def __init__(self, API_KEY):
        self.API_KEY = API_KEY
        self.model = genai.GenerativeModel("gemini-1.5-flash")
        genai.configure(api_key=API_KEY)

    def num_response(self, x: int) -> str:
        """Generates a response indicating if the given number is odd.

        Args:
            x (int): The number to be checked

        Returns:
            str: 'yes' if the number is odd, 'no' otherwise.
        """

        prompt = self.PROMPT.format(x)
        response = self.model.generate_content(prompt)
        return response.text


