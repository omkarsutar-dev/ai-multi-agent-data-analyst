import requests

API_URL = "http://127.0.0.1:8000/analyze"

def analyze_query(query):
    try:
        response = requests.post(API_URL, json={"query": query})
        print("Status:", response.status_code)
        print("Response:", response.text)   # 🔥 IMPORTANT
        return response.json()
    except Exception as e:
        print("Error:", e)
        return {"insight": "API Error"}