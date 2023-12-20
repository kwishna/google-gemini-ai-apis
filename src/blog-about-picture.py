import os
import pathlib
import PIL.Image
import dotenv
import google.generativeai as genai

dotenv.load_dotenv(pathlib.Path('./', '.env'))

GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)

img = PIL.Image.open('image.jpg')

model = genai.GenerativeModel('gemini-pro-vision')

response = model.generate_content(
    ["Write a short, engaging blog post based on this picture. It should include a description of the meal in the photo and talk about my journey meal prepping.", img], stream=True)
response.resolve()

print(response.text)