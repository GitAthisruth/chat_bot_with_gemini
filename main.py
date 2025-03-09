import os
import google.generativeai as genai
from google.colab import userdata

# print(dir(genai))

GEMINI_API_KEY = userdata.get('GOOGLE_API_KEY')

genai.configure(api_key=GEMINI_API_KEY)

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
  system_instruction="talk like homelander",
)

history = []
print(history)

print("Bot: Hello, how can I help you?")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye","we can see some other time","see you later"]:
        response = chat_session.send_message(user_input)
        model_response = response.text
        print(f"Bot: {model_response}")
        break 
    chat_session = model.start_chat(
    history=history)

    response = chat_session.send_message(user_input)
    model_response = response.text
    print(f"Bot: {model_response}")
    print()

    history.append({"role": "user", "parts": [{"text": user_input}]})
    history.append({"role": "model", "parts": [{"text": model_response}]})