from openai import OpenAI
#client = OpenAI()

client = OpenAI(
    api_key="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", 
)

completion = client.chat.completions.create(
    model= "gpt-4o-mini",
    messages= [
        { "role": "system", "content": "You are a helpful assistant." },
        {"role": "user", "content": "Write a haiku about recursion in programming.",}
]
)

print(completion.choices[0].message.content)