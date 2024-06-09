import pyttsx3

text = "你好，世界！这是一个文字转语音的示例。"
text = "Hello! Nice to meet you. I am an AI assistant for mindfulness exercises."

engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()