import openai
import requests
import os

# 设置 OpenAI API 密钥
openai.api_key = 'sk-proj-Bue2ofTbTAvx2ExJvNGdT3BlbkFJqvLfVmmvjcveUaEpQoGS'

# 调用 OpenAI API 生成图片
response = openai.Image.create(prompt="一只愤怒的猫捉老鼠", n=1, size="1024x1024")

# 获取图片链接
image_url = response['data'][0]['url']

# 发送 HTTP 请求获取图片内容
image_response = requests.get(image_url)

# 检查请求是否成功
if image_response.status_code == 200:
    with open('generated_image.jpg', 'wb') as file:
        file.write(image_response.content)
    print('图片已成功保存为 "generated_image.jpg"')
else:
    print('无法获取图片:', image_response.status_code)