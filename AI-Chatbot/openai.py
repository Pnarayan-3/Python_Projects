from openai import OpenAI

#pip install openai

client=OpenAI(
    api_key="put your own api key",
)

command='''
chat from message app
'''


completion=client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role":"system","content":"you are a person named piyush who speaks hindi as well as english. "
        "he is from India and is a coder.You analyze chat history and respond like piyush "},
        {"role":"user","content":command}
    ]
)

print(completion.choices[0].message)