from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

prompt = "Write a short paragraph about Artificial Intelligence"

response = client.responses.create(
    model="gpt-3.5-turbo-instruct",
    input=prompt,
    max_output_tokens=100
)

print(response.output_text)
