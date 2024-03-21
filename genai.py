import os
import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

genai.configure(api_key="AIzaSyDU0F3ZmGWBrrFpmUv21ZHuJBoTbtm4mL8")

import PIL.Image

img = PIL.Image.open('bar.png')
model = genai.GenerativeModel('gemini-pro-vision')
response = model.generate_content(img)

response = model.generate_content(["You are a professional Data Analyst, write the complete conclusion and actionable insight based on the image", img], stream=True)
response.resolve()
print(response.text)

