from ollama import chat

response = chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "user",
            "content": "Explain why sales may decrease over time."
        }
    ]
)

print(response["message"]["content"])