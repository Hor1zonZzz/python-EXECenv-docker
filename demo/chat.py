from openai import OpenAI
from dotenv import load_dotenv
import re

load_dotenv()

def extract_code(md_content):
    code = re.split('```[a-zA-Z0-9- ]*', md_content, maxsplit=10)[1]
    return code

client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4o-2024-08-06",
  messages=[
    {"role": "system", "content": "You are a helpful code assistant."},
    {"role": "user", "content": "write a simple executable code in python, meanwhile dont need user to input"}
  ]
)

result = response.choices[0].message.content
print(result)

code = extract_code(result)
print(code)

with open("scriptdemo.py", 'w') as file:
    file.write(code)
    print("文件已经写入")

import codeInterpreterDocker

codeInterpreterDocker.codeInterpreter()
