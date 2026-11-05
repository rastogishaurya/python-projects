import requests
def ask_ai(prompt):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "llama3.2:3b",
        "prompt": prompt,
        "stream": False,    
    }

    response = requests.post(url, json=payload)
    data = response.json()
    return(data["response"])

ans = ask_ai("Explain what a Python dictionary is in two sentences.")
print(ans)