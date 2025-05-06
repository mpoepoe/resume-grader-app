import openai

# 1️⃣ Set your API key
openai.api_key = "YOUR_API_KEY"

# 2️⃣ Call the chat completion endpoint
response = openai.ChatCompletion.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user",   "content": "What's the weather like in Paris today?"}
    ]
)

# 3️⃣ Print the assistant’s reply
print(response.choices[0].message.content)
