import os
import pathlib
import dotenv
import google.generativeai as genai

dotenv.load_dotenv(pathlib.Path('../', '.env'))

GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

"""## Advanced use cases

The following sections discuss advanced use cases and lower-level details of the Python SDK for the Gemini API.

### Safety settings

The `safety_settings` argument lets you configure what the model blocks and allows in both prompts and responses. By default, safety settings block content with medium and/or high probability of being unsafe content across all dimensions. Learn more about [Safety settings](https://ai.google.dev/docs/safety_setting).

Enter a questionable prompt and run the model with the default safety settings, and it will not return any candidates:
"""

response = model.generate_content('[Questionable prompt here]')
print(response.candidates)

"""The `prompt_feedback` will tell you which safety filter blocked the prompt:"""

print(response.prompt_feedback)

"""Now provide the same prompt to the model with newly configured safety settings, and you may get a response."""

response = model.generate_content('[Questionable prompt here]', safety_settings={'HARASSMENT':'block_none'})
print(response.text)