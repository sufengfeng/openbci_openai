import openai
import time
import openai
import requests
import os

# response = openai.Completion.create(model="text-davinci-002", prompt="Say this is a test", temperature=0, max_tokens=7)

def openai_chatgpt_function():
    pass

if __name__ == "__main__":
    question = "西游记是谁写的？"
    print("问题:{}".format(question))
    url = "https://api.openai.com/v1"  # 可以替换为任何代理的接口
    # OPENAI_API_KEY="sk-LECc8U0BcVAQWx1VE23aB8B5595f4963929d799b712382E3"  # openai官网获取key
    # openai.api_key = OPENAI_API_KEY
    # openai.api_base = openai_url
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": question}], stream=False)

    print("完整的响应结果:{}".format(response))
    answer = response.choices[0].message.content
    print("答案:{}".format(answer))