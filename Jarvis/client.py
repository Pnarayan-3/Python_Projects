from openai import OpenAI

#pip install openai

client=OpenAI(
    api_key="put your own api key",
)

completion=client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role":"system","content":"you are a virtual assistant named Jarvis ,skilled in general tasks like alexa and Google Cloud"},
        {"role":"user","content":"what is coding"}
    ]
)

print(completion.choices[0].message)