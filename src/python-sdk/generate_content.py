import os
import pathlib
import dotenv
import google.generativeai as genai

dotenv.load_dotenv(pathlib.Path('../', '.env'))

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("What is the meaning of life?")

print(response.text)
print("----------------------------------------------------------------------------------------------------------------")
print(response.prompt_feedback)
print("----------------------------------------------------------------------------------------------------------------")
print(response.candidates)
print("----------------------------------------------------------------------------------------------------------------")
