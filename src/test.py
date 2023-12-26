import requests
import json

API_KEY = "sk-ebFpoJCkwwpUhoyjFadXTBlbkFJluawMDF0hlVghCfiBYgW"  # Replace with your actual OpenAI API key
prompt = """ 

Определи к какому типу отнсосится сообщение 'у меня проблемы с девушкой' из типов, ответ дай в формате цифра, точка и тип:

1. Отношения с родителями и семьей
2. Отношения со сверстниками (дружеские)
3. Отношения с социумом
4. Отношения с противоположным полом
5. Обучение в школе, подготовка к вузу
6. Профориентация, самопознание,  целеполагание
7. Самооценка, саморазвитие
8. Здоровье, красота, полезные и вредные привычки, зависимости
9. Индивидуальные кризисные ситуации

"""

APIBody = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {"role": "user", "content": prompt}
    ]
}

response = requests.post(
    "https://api.openai.com/v1/chat/completions",
    headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    },
    data=json.dumps(APIBody)
)

data = response.json()
print(data)