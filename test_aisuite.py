import unittest
from unittest.mock import patch, MagicMock
import aisuite as ai
from dotenv import load_dotenv

load_dotenv()

class TestAISuite(unittest.TestCase):
    def test_ai_suite_call(self):
        # Load API keys from the configuration or environment variables
 
        client = ai.Client( )  # Call the AI suite with the API key
        request_data = [{"role": "user", "content": "Test input"}]  # Example request data
        response = client.chat.completions.create(model="groq:llama-3.1-8b-instant", messages=request_data)  # Make a request to the AI suite
        response_content = response.choices[0].message.content
        
        # Print the response for verification
        print("Response:", response_content)
        
        # Verify output and parse it
        self.assertIsNotNone(response)  # Check if the response is not None


    def test_gpt_call(self):
        # Call the get_chatgpt_response function from main.py
        from AI_call import get_chatgpt_response
        
        test_input = "Hello, how are you?"  # Example input text
        response_text = get_chatgpt_response(test_input)  # Call the function
        
        # Verify that the response is a non-empty string
        self.assertIsInstance(response_text, str)  # Check if the response is a string
        self.assertTrue(len(response_text) > 0)  # Ensure the response is not empty
if __name__ == '__main__':
    cls = TestAISuite()
    # cls.test_ai_suite_call() 

    cls.test_gpt_call()