import unittest
from unittest.mock import patch
 
from AI_call import call_ai_with_tools

class TestProcessQueryTools(unittest.TestCase):
    
    def test_process_query_tools(self):
        # Arrange
        test_input = "Can you tell me about my experience in ai ml from resume /cv ?"
        test_input = "Tell me my experience at Nvidia from my resume."
        test_input = "what is digital wallet project from Resume."
        # Act
        response = call_ai_with_tools(test_input)
        # response = process_query_tools(test_input)
        
        # Print the response for verification
        print(response)
    
    def test_process_query_tools_user_info(self):
        # Arrange
        test_input = "Can you tell me about my hobbies from personal file?"
        test_input ="What's users #1 superpower?"
        # test_input ="What are the top 3 areas you’d like to grow in?"
        # test_input ="What misconception do your coworkers have about you?"
        # Act
        response = call_ai_with_tools(test_input)
        
        
        # Print the response for verification
        print(response)
 
if __name__ == '__main__':
    TestProcessQueryTools().test_process_query_tools_user_info()
    # TestProcessQueryTools().test_process_query_tools()
       