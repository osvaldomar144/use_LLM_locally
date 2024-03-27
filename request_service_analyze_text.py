import requests

url = "http://10.20.40.22:8005/analyze_text"

text = {
  "data": "President Ashraf Ghani has maintained a pro-US and pro-Western stance, but his relations with the US are likely to become strained because of US pressure to conclude a domestic peace deal with the Taliban that will enable full US military withdrawal from Afghanistan in 2021. Relations with Pakistan are likely to remain poor given deep Afghan suspicions about Pakistan's support for the Taliban. Relations with China and Iran will remain cordial, but strong US relations remain Ghani's primary foreign policy priority, and he will avoid foreign engagements that might be viewed unfavourably by Washington."
}

request = requests.post(url, json=text)

if request.status_code == 200:
    response = request.json()
    print(response)
else:
    print(f"Errore: {request.status_code}")
