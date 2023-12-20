import os
import pathlib
import dotenv
import google.generativeai as genai

dotenv.load_dotenv(pathlib.Path('../', '.env'))

GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

response = chat.send_message("In one sentence, explain how a computer works to a young child.")

print("------------< response.text >----------------")
print(response.text)
print("------------< chat.history >----------------")
print(chat.history)
print("----------------------------")

response = chat.send_message("Okay, how about a more detailed explanation to a high schooler?", stream=True)

for chunk in response:
  print(chunk.text)
  print("-"*40 + '< chunk.text >' + "-"*40)

"""`glm.Content` objects contain a list of `glm.Part` objects that each contain either a text (string) or inline_data (`glm.Blob`), where a blob contains binary data and a `mime_type`. The chat history is available as a list of `glm.Content` objects in `ChatSession.history`:"""

for idx, message in enumerate(chat.history):
  print(f"{'-'*40} {idx} {'-'*40}")
  print(f'**{message.role}**: {message.parts[0].text}')