import openai 

openai.api_key=""
#client = OpenAI()
messages = []
system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready!")
while True:
    message = input()
    if message == "quit()":
        break
    messages.append({"role": "user", "content": message})
    response = openai.chat.completions.create(model="gpt-3.5-turbo",
    #response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=messages)
    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")
