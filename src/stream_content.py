import os
import pathlib
import dotenv
import google.generativeai as genai

dotenv.load_dotenv(pathlib.Path('./', '.env'))

GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("What is the meaning of life?", stream=True)
for chunk in response:
  print(chunk.text)
  print("_"*80)

"""When streaming, some response attributes are not available until you've iterated through all the response chunks. This is demonstrated below:"""

response = model.generate_content("What is the meaning of life?", stream=True)

print(response.prompt_feedback)

try:
  print(response.text)
except Exception as e:
  print(f'{type(e).__name__}: {e}')