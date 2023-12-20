import os
import pathlib
import dotenv
import google.generativeai as genai

dotenv.load_dotenv(pathlib.Path('./', '.env'))

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)

"""## List models

Now you're ready to call the Gemini API. Use `list_models` to see the available Gemini models:

* `gemini-pro`: optimized for text-only prompts.
* `gemini-pro-vision`: optimized for text-and-images prompts.
"""

print(list(genai.list_models()))
print("----------------------------------------------------------------------------------------------------------------")

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(f"'generateContent' is present in {m.name}.")