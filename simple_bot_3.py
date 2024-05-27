import openai
import gradio as gr

openai.api_key = ""

messages = [{"role": "system", "content": "You are personal assitant that helps businessman with everyday tasks and gives them advice on how to improve their business."}]

def CustomChatGPT(user_input):
    try:
        messages.append({"role": "user", "content": user_input})
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        ChatGPT_reply = response.choices[0].message.content
        messages.append({"role": "assistant", "content": ChatGPT_reply})
        return ChatGPT_reply
    except Exception as e:
        return str(e)

demo = gr.Interface(fn=CustomChatGPT, inputs="text", outputs="text", title="Personal Chatbot")

demo.launch(share=True)
