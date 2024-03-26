import textwrap
import google.generativeai as genai

from getpass import getpass
import os

GOOGLE_API_KEY = getpass('Enter the secret value: ')

genai.configure(api_key=GOOGLE_API_KEY)

#modelli disponibili
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print("\n " + m.name)

generation_config = {
    "temperature": 0.8,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

model = genai.GenerativeModel('gemini-pro', generation_config=generation_config)
response = model.generate_content("Dame el codigo de un dataframe de pandas para sacar la diferencia de dias entre fechas de datetime64[ns]")
print("\n _____________Response:_________________________ \n" + response.text)
