#!/usr/bin/python3
# -*- coding: utf-8 -*-
import logging
import os
import sys
import random
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo

from ui.main_window import Ui_MainWindow

# def ReceiveData(name,_self):
#     while _self.m_bIsRunning:

from ctypes import *
# import xlwt

from ui_py.ui_setup import Setup_Dialog
from ui_py.ui_waveform import QCustomPlotWaveform

_READ = 0

logging.basicConfig(
    format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d:%H:%M:%S',
    level=logging.DEBUG
)

logger = logging.getLogger(__name__)

import sys
import time

import datetime

import re

import qdarkstyle

questionList = [
    "Hello! Nice to meet you. I am an AI assistant for mindfulness exercises. ",
    "continue",
    "You must have come to me because you want to try some mindfulness exercises, right?",
    "continue",
    "Great! Mindfulness exercises are my specialty. We need to take some time to prepare before we start practicing.",
    "The first step in preparation is to find a quiet and comfortable environment where you won't be disturbed.",
    "Please prepare a pen and paper. I will need you to record some of your own information during the exercise.",
    "Choose a comfortable posture in your environment. ",
    "You can stand, sit, or lie down. The only thing to note is to keep your spine straight.",
    "Try to relax and focus on your breathing. ",
    "Now inhale (silently count to 5), exhale through your mouth (silently count to 8), inhale (silently count to 5), exhale (silently count to 8), inhale (silently count to 5), exhale (silently count to 8).",
    "If you feel relaxed and ready to start the exercise, please let me know.",
    "continue",
    "Let's get to know each other first. Let's play a game. We will draw a card and use it to introduce one aspect of ourselves. I'll demonstrate first. ",
    "On the card I drew, I saw children and adults holding hands. This picture evokes the warm feeling of companionship and being accompanied in life. ",
    "Now I introduce myself: As an AI assistant in mental health software, I communicate with users. This card reminds me that sometimes I play the role of an adult in communication, and sometimes I play the role of a child to talk to users. ",
    "I strive to be their trusted companion, helping them identify their feelings and needs through listening and understanding, so as to better regulate their emotions and cope with the challenges in life. ",
    "Now it's your turn. Here is a set of cards. Please choose any one. After choosing it, you can substitute into the card to introduce yourself to me, okay?",
    "continue",
    "What do you see on this card?",
    "continue",
    "OK, you see this card. Now by using your imagination, in the scene, please introduce yourself to me according to the card. Alright, now I know you.",
    "I am very happy to accompany you to do this exercise today. Next, we will use the same game to become aware of our emotions. Are you ready?",
    "continue",
    "Before we do emotional awareness, it is essential to understand and experience our own existence. ",
    "Without a clear understanding of one's own existence, emotional awareness may be baseless, like a castle in the air. Please draw another card now and tell a story related to your own experience, which is based on \"yourself\" or with \"I\" as the subject. ",
    "Now you can observe the space around you, look at the colors, shapes, and sizes here. Experience yourself as an observer while observing. ",
    "Then close your eyes and let the thought of \"you are an observer\" arise. Still maintain the observer's state. ",
    "Thoughts and emotions, like the shapes and sizes in the room, become our objects of observation, letting them come and go freely, without our participation.",
    "In this process, the content observed is not important; what matters is experiencing yourself as an observer through observation. ",
    "Through such observations, you can dissociate and no longer have direct emotional connections with these external or internal phenomena but look at them as an observer. Do you understand what I mean?",
    "continue",
    "Now that you understand how to feel your existence from the perspective of an observer, you did a great job. ",
    "Let's do an observer exercise first, so that the feeling of (emotion) has a chance to appear, okay? ",
    "continue",
    "Now please gently close your eyes, or you can keep them open. Visualize a scene that makes you feel very relaxed. ",
    "This scene could be on a beach by the sea, in a castle, in a garden, etc. Now please describe the scene to me. ",
    "If none of them, then describe the style you have in mind like I did. Now write down your description. Please tell me when you have recorded it:",
    "What is the weather like in the scene? How is the air? How are the surroundings? What time of day is it? What sounds can you hear? I've painted some scenes for you now, which style do you prefer? ",
    "continue",
    "Please draw another card now and tell a story related to your own experience, which is based on \"yourself\" or with \"I\" as the subject. Please write this story down on paper.",
    "continue",
    "How do you feel when you see these scenes? Please write it down",
    "continue",
    "Very good, you describe it clearly. When describing this situation, do you have a stronger feeling of (emotion)?",
    "continue",
    "Then let's be with this feeling of (emotion). Please keep recalling the scene at that time and let this feeling of (emotion) happen as it shows. Do you think this feeling is strong enough?",
    "continue",
    "If you think the intensity of this feeling is not strong enough, you can also gently close your eyes to make the feeling stronger. ",
    "Imagine the weather at that time, the people around you, the scene, what you were doing, and what you were about to do. Please write it down.",
    "continue",
    "As you keep recalling this scene, does your feeling of (emotion) become more evident?",
    "continue",
    "You are doing very well. Now observe: When the feeling of (emotion) arises, what subtle changes occur in your body on a physiological level? Please write it down",
    "continue",
    "You are doing very well. Please maintain this feeling of (emotion), letting it continuously arise.",
    "As an observer, you can imagine yourself as a mirror, reflecting the feeling of (emotion) continuously arising. Or you can imagine yourself as a beam of light, shining from afar on this feeling, letting it continuously arise.",
    "continue",
    "Hold on for a while and see if this feeling undergoes subtle changes. See if it becomes stronger, fades away slowly, or remains unchanged in intensity. ",
    "During this process, you can also try to capture the thoughts in your mind and see what kind of images and thoughts you capture. Please write down the thoughts and images you captured",
    "continue",
    "As you maintain this stance, feel that there is a very (emotion) self inside you. This (emotion) self will appear in your life and be noticed by you at certain moments in your life, just like now. ",
    "Now let's invite this very (emotion) self to the scene of nature you just chose. Can you see the (emotion) self in the scene now?",
    "continue",
    "Can you tell me how old you are in this scene? What are your attire and appearance like? Please write it down",
    "continue",
    "Now allow him/her to come to your natural scene, allowing him/her to run freely on this grass. You can also allow him/her to sit quietly.",
    "continue",
    "You can imagine the sun shining quietly on yourself. You can imagine the sun shining quietly on yourself. (Concrete comfortable sensation makes your emotions feel safe) ",
    "Now you can imagine that the sunshine also shines on your head. ",
    "It shines into your cranial cavity, making it warm and very comfortable. ",
    "The sun continues to shine on your chest, making it warm and very comfortable. ",
    "The sun continues to shine on your abdominal cavity, making it warm and very comfortable. ",
    "The sun continues to shine on your limbs, making them warm and very comfortable. ",
    "If you are willing, please give him/her a name. And write it down. ",
    "continue",
    "Now please allow him/her to run freely in your scene as it is. ",
    "You can imagine that you are surrounded by a soft, pure, and warm light from head to toe, like a beautiful angel walking beside him/her.",
    "continue",
    "Now you can try to talk and chat with him/her and get to know him/her. I am curious, what do you want to say to him/her? Please write it down.",
    "continue",
    "Okay, so how would he/she respond to you? Please write it down.",
    "continue",
    "Very good. Now you can imagine chatting with him/her, and you can write down what you talked about.",
    "continue",
    "Very good, now please play with him/her. He/she represents the (emotion) in your heart and often generates this emotion. ",
    "Now he/she has come to this scene, and now you can accompany him/her. Just pause for a moment.",
    "continue",
    "When you play with him/her, how do you feel? How does he/she feel? Please write it down.",
    "continue",
    "Very good, when he/she doesn't want to play anymore and wants to do other things, such as chatting, lying down, sunbathing, etc., just tell me.",
    "continue",
    "Now can you tell me what you want to say to him/her or what he/she wants to say to you? Please write it down.",
    "continue",
    "Observe him/her seriously. Usually, his/her emotions are so intense that whenever you encounter a certain situation, such as the scenarios you wrote earlier, or other situations you might face, he/she will come into your life to express himself/herself.",
    "I am curious, from childhood to now, what kind of situations generally appear when he/she comes into your life and gets noticed by you?",
    "Specifically, in what situations and contexts does he/she come out to express himself/herself? Please write it down.",
    "continue",
    "I see.",
    "In these situations, when he/she comes into your life, what exactly does he/she want to remind you of or what kind of message does he/she want to convey?",
    "continue",
    "I get it. (ChatGPT - Rationalizing Emotional Presence) Let's try to understand. In the case of “----”, he/she is present to “----” you. He/she doesn't want you to go through the “----” situation because he/she thinks that something bad “----” might happen. He/she will try to “----” you and “----” you in his/her own way. Do you agree?",
    "continue",
    "In the situation you associate with, you see this scene and associate it with similar scenarios happening to you, making you feel very uncomfortable.",
    "So he/she uses his/her feelings to remind you that this is a situation you don't want to experience. He/she uses this way to remind you and protect you, right?",
    "continue",
    "Very good!",
    "Now you understand his/her function. He/she will naturally jump out to protect you in situations that might make you feel uncomfortable. ",
    "This feeling has been there from a very young age until now and will continue every day in the future. I guess only your best friend would come out to express your feelings when you are uncomfortable, right?",
    "continue",
    "Alright, now we understand that Robert is actually your good friend. He/she comes out to express your feelings when you face certain dangerous situations.",
    "I am curious, is there any misunderstanding between you and him/her that needs to be clarified?",
    "continue",
    "Why don't you invite him/her to come and talk with you? Are you interested in chatting with him/her?",
    "continue",
    "Would he/she also be interested in chatting with you?",
    "continue",
    "Alright, please invite him/her to your side. Now, please express your misunderstanding to him/her. I am curious, how would you ask him/her?",
    "continue",
    "When you ask him/her this way, how would he/she respond?",
    "continue",
    "How would you respond to him/her then?",
    "continue",
    "Great. When he/she says that, how would you respond?",
    "continue",
    "You can ask him/her: What can I do to make you feel better?",
    "continue",
    "Is this his/her expression?",
    "continue",
    "Very good. When he/she gives you this suggestion, how would you respond?",
    "continue",
    "When you respond this way, how would he/she answer you?",
    "continue",
    "I see. Now you can tell him/her: There are some situations, people, and events that I must face. When I face them, what can I do to comfort, understand, or support you to make you feel better?",
    "continue",
    "Now let's try to fully understand him/her and appreciate his/her presence. Understand that he/she is a good friend who came into your life when you were very young. Whenever you perceive danger, he/she stands up to express himself/herself.",
    "Whenever he/she appears, you understand him/her and appreciate his/her loyal presence.",
    "How does he/she feel now?",
    "continue",
    "Alright. Now, you can try to gently hug him/her. Place your left hand on your right arm and your right hand on your left arm, gently hugging yourself.",
    "When you hug yourself, you can try to gently tell him/her: Dear, you’ve worked hard, and I thank you very much. No matter what happens, I will love you unconditionally.",
    "When you sincerely love him/her, please imagine that he/she will respond to you with love as well.",
    "Imagine that the energy of love will slowly flow in your chest.",
    "Now please imagine that the sun still shines quietly on your head.",
    "It shines into your cranial cavity, warm and very comfortable.",
    "The sun continues to shine on your chest, warm and very comfortable.",
    "The sun continues to shine on your abdominal cavity, warm and very comfortable.",
    "Later, when you open your eyes, whenever he/she comes into your life and gets noticed by you, you can gently hug yourself like this.",
    "When you hug yourself, he/she will feel understood, appreciated, and loved. He/she has completed the task of conveying the signal.",
    "He/she will try to let go of his control and will fully encourage you to follow your inner guidance. Whenever he/she appears, you can gently hug yourself.",
    "Now, you can imagine him/her slowly merging with you. The two of you are originally one person. He/she is originally a part of your life. When a certain situation arises, he will stand up to express himself.",
    "As long as you hug yourself gently, he will feel understood, supported, loved, and appreciated.",
    "He/she will give back the leadership of life to you.",
    "Now, you can still look at the situation quietly, open your eyes, and return to the present.",
    "How do you feel now?",
    "continue",
    "Alright, try this in the future. If you encounter a situation that makes you feel uncomfortable, gently hug yourself like this. Then follow your inner feelings. ",
    "He/she just needs to be understood, comforted, loved, appreciated, hugged, or accompanied. ",
    "As long as he/she feels all this, his/her mission is complete, and he/she will give back the leadership to you, no longer interfering or affecting you.",
    "Congratulations on completing this awareness exercise, you did a great job!",
]
questionList = [
    "Hello! Nice to meet you. I am an AI assistant for mindfulness exercises. ",
    # "continue",
    "You must have come to me because you want to try some mindfulness exercises, right?",
    "continue",
    "Great! Mindfulness exercises are my specialty. We need to take some time to prepare before we start practicing.",
    # "The first step in preparation is to find a quiet and comfortable environment where you won't be disturbed.",
    # "Please prepare a pen and paper. I will need you to record some of your own information during the exercise.",
    # "Choose a comfortable posture in your environment. ",
    # "You can stand, sit, or lie down. The only thing to note is to keep your spine straight.",
    # "Try to relax and focus on your breathing. ",
    # "Now inhale (silently count to 5), exhale through your mouth (silently count to 8), inhale (silently count to 5), exhale (silently count to 8), inhale (silently count to 5), exhale (silently count to 8).",
    # "If you feel relaxed and ready to start the exercise, please let me know.",
    # "continue",
    # "Let's get to know each other first. Let's play a game. We will draw a card and use it to introduce one aspect of ourselves. I'll demonstrate first. ",
    # "On the card I drew, I saw children and adults holding hands. This picture evokes the warm feeling of companionship and being accompanied in life. ",
    # "Now I introduce myself: As an AI assistant in mental health software, I communicate with users. This card reminds me that sometimes I play the role of an adult in communication, and sometimes I play the role of a child to talk to users. ",
    # "I strive to be their trusted companion, helping them identify their feelings and needs through listening and understanding, so as to better regulate their emotions and cope with the challenges in life. ",
    # "Now it's your turn. Here is a set of cards. Please choose any one. After choosing it, you can substitute into the card to introduce yourself to me, okay?",
    # "continue",
    # "What do you see on this card?",
    # "continue",
    # "OK, you see this card. Now by using your imagination, in the scene, please introduce yourself to me according to the card. Alright, now I know you.",
    # "I am very happy to accompany you to do this exercise today. Next, we will use the same game to become aware of our emotions. Are you ready?",
    # "continue",
    # "Before we do emotional awareness, it is essential to understand and experience our own existence. ",
    # "Without a clear understanding of one's own existence, emotional awareness may be baseless, like a castle in the air. Please draw another card now and tell a story related to your own experience, which is based on \"yourself\" or with \"I\" as the subject. ",
    # "Now you can observe the space around you, look at the colors, shapes, and sizes here. Experience yourself as an observer while observing. ",
    # "Then close your eyes and let the thought of \"you are an observer\" arise. Still maintain the observer's state. ",
    # "Thoughts and emotions, like the shapes and sizes in the room, become our objects of observation, letting them come and go freely, without our participation.",
    # "In this process, the content observed is not important; what matters is experiencing yourself as an observer through observation. ",
    # "Through such observations, you can dissociate and no longer have direct emotional connections with these external or internal phenomena but look at them as an observer. Do you understand what I mean?",
    # "continue",
    # "Now that you understand how to feel your existence from the perspective of an observer, you did a great job. ",
    # "Let's do an observer exercise first, so that the feeling of (emotion) has a chance to appear, okay? ",
    # "continue",
    # "Now please gently close your eyes, or you can keep them open. Visualize a scene that makes you feel very relaxed. ",
    # "This scene could be on a beach by the sea, in a castle, in a garden, etc. Now please describe the scene to me. ",
    # "If none of them, then describe the style you have in mind like I did. Now write down your description. Please tell me when you have recorded it:",
    "What is the weather like in the scene? How is the air? How are the surroundings? What time of day is it? What sounds can you hear? I've painted some scenes for you now, which style do you prefer? ",
    "continue",
    "mask_getpic_from_word",
    # "Please draw another card now and tell a story related to your own experience, which is based on \"yourself\" or with \"I\" as the subject. Please write this story down on paper.",
    # "continue",
    # "How do you feel when you see these scenes? Please write it down",
    # "continue",
    # "Very good, you describe it clearly. When describing this situation, do you have a stronger feeling of (emotion)?",
    # "continue",
    # "Then let's be with this feeling of (emotion). Please keep recalling the scene at that time and let this feeling of (emotion) happen as it shows. Do you think this feeling is strong enough?",
    # "continue",
    # "If you think the intensity of this feeling is not strong enough, you can also gently close your eyes to make the feeling stronger. ",
    # "Imagine the weather at that time, the people around you, the scene, what you were doing, and what you were about to do. Please write it down.",
    # "continue",
    # "As you keep recalling this scene, does your feeling of (emotion) become more evident?",
    # "continue",
    # "You are doing very well. Now observe: When the feeling of (emotion) arises, what subtle changes occur in your body on a physiological level? Please write it down",
    # "continue",
    # "You are doing very well. Please maintain this feeling of (emotion), letting it continuously arise.",
    # "As an observer, you can imagine yourself as a mirror, reflecting the feeling of (emotion) continuously arising. Or you can imagine yourself as a beam of light, shining from afar on this feeling, letting it continuously arise.",
    # "continue",
    # "Hold on for a while and see if this feeling undergoes subtle changes. See if it becomes stronger, fades away slowly, or remains unchanged in intensity. ",
    # "During this process, you can also try to capture the thoughts in your mind and see what kind of images and thoughts you capture. Please write down the thoughts and images you captured",
    # "continue",
    # "As you maintain this stance, feel that there is a very (emotion) self inside you. This (emotion) self will appear in your life and be noticed by you at certain moments in your life, just like now. ",
    "Now let's invite this very (emotion) self to the scene of nature you just chose. Can you see the (emotion) self in the scene now?",
    "continue",
    "Can you tell me how old you are in this scene? What are your attire and appearance like? Please write it down",
    "continue",
    "mask_getpic_from_word",
    # "Now allow him/her to come to your natural scene, allowing him/her to run freely on this grass. You can also allow him/her to sit quietly.",
    # "continue",
    # "You can imagine the sun shining quietly on yourself. You can imagine the sun shining quietly on yourself. (Concrete comfortable sensation makes your emotions feel safe) ",
    # "Now you can imagine that the sunshine also shines on your head. ",
    # "It shines into your cranial cavity, making it warm and very comfortable. ",
    # "The sun continues to shine on your chest, making it warm and very comfortable. ",
    # "The sun continues to shine on your abdominal cavity, making it warm and very comfortable. ",
    # "The sun continues to shine on your limbs, making them warm and very comfortable. ",
    # "If you are willing, please give him/her a name. And write it down. ",
    # "continue",
    # "Now please allow him/her to run freely in your scene as it is. ",
    # "You can imagine that you are surrounded by a soft, pure, and warm light from head to toe, like a beautiful angel walking beside him/her.",
    # "continue",
    # "Now you can try to talk and chat with him/her and get to know him/her. I am curious, what do you want to say to him/her? Please write it down.",
    # "continue",
    # "Okay, so how would he/she respond to you? Please write it down.",
    # "continue",
    # "Very good. Now you can imagine chatting with him/her, and you can write down what you talked about.",
    # "continue",
    # "Very good, now please play with him/her. He/she represents the (emotion) in your heart and often generates this emotion. ",
    # "Now he/she has come to this scene, and now you can accompany him/her. Just pause for a moment.",
    # "continue",
    # "When you play with him/her, how do you feel? How does he/she feel? Please write it down.",
    # "continue",
    # "Very good, when he/she doesn't want to play anymore and wants to do other things, such as chatting, lying down, sunbathing, etc., just tell me.",
    # "continue",
    # "Now can you tell me what you want to say to him/her or what he/she wants to say to you? Please write it down.",
    # "continue",
    # "Observe him/her seriously. Usually, his/her emotions are so intense that whenever you encounter a certain situation, such as the scenarios you wrote earlier, or other situations you might face, he/she will come into your life to express himself/herself.",
    # "I am curious, from childhood to now, what kind of situations generally appear when he/she comes into your life and gets noticed by you?",
    # "Specifically, in what situations and contexts does he/she come out to express himself/herself? Please write it down.",
    # "continue",
    "I see.",
    "In these situations, when he/she comes into your life, what exactly does he/she want to remind you of or what kind of message does he/she want to convey?",
    "continue",
    "I get it. (ChatGPT - Rationalizing Emotional Presence) Let's try to understand. In the case of “----”, he/she is present to “----” you. He/she doesn't want you to go through the “----” situation because he/she thinks that something bad “----” might happen. He/she will try to “----” you and “----” you in his/her own way. Do you agree?",
    "continue",
    "mask_getpic_from_word",
    # "In the situation you associate with, you see this scene and associate it with similar scenarios happening to you, making you feel very uncomfortable.",
    # "So he/she uses his/her feelings to remind you that this is a situation you don't want to experience. He/she uses this way to remind you and protect you, right?",
    # "continue",
    # "Very good!",
    # "Now you understand his/her function. He/she will naturally jump out to protect you in situations that might make you feel uncomfortable. ",
    # "This feeling has been there from a very young age until now and will continue every day in the future. I guess only your best friend would come out to express your feelings when you are uncomfortable, right?",
    # "continue",
    # "Alright, now we understand that Robert is actually your good friend. He/she comes out to express your feelings when you face certain dangerous situations.",
    # "I am curious, is there any misunderstanding between you and him/her that needs to be clarified?",
    # "continue",
    # "Why don't you invite him/her to come and talk with you? Are you interested in chatting with him/her?",
    # "continue",
    # "Would he/she also be interested in chatting with you?",
    # "continue",
    # "Alright, please invite him/her to your side. Now, please express your misunderstanding to him/her. I am curious, how would you ask him/her?",
    # "continue",
    # "When you ask him/her this way, how would he/she respond?",
    # "continue",
    # "How would you respond to him/her then?",
    # "continue",
    # "Great. When he/she says that, how would you respond?",
    # "continue",
    # "You can ask him/her: What can I do to make you feel better?",
    # "continue",
    # "Is this his/her expression?",
    # "continue",
    # "Very good. When he/she gives you this suggestion, how would you respond?",
    # "continue",
    # "When you respond this way, how would he/she answer you?",
    # "continue",
    # "I see. Now you can tell him/her: There are some situations, people, and events that I must face. When I face them, what can I do to comfort, understand, or support you to make you feel better?",
    # "continue",
    # "Now let's try to fully understand him/her and appreciate his/her presence. Understand that he/she is a good friend who came into your life when you were very young. Whenever you perceive danger, he/she stands up to express himself/herself.",
    # "Whenever he/she appears, you understand him/her and appreciate his/her loyal presence.",
    # "How does he/she feel now?",
    # "continue",
    # "Alright. Now, you can try to gently hug him/her. Place your left hand on your right arm and your right hand on your left arm, gently hugging yourself.",
    # "When you hug yourself, you can try to gently tell him/her: Dear, you’ve worked hard, and I thank you very much. No matter what happens, I will love you unconditionally.",
    # "When you sincerely love him/her, please imagine that he/she will respond to you with love as well.",
    # "Imagine that the energy of love will slowly flow in your chest.",
    # "Now please imagine that the sun still shines quietly on your head.",
    # "It shines into your cranial cavity, warm and very comfortable.",
    # "The sun continues to shine on your chest, warm and very comfortable.",
    # "The sun continues to shine on your abdominal cavity, warm and very comfortable.",
    # "Later, when you open your eyes, whenever he/she comes into your life and gets noticed by you, you can gently hug yourself like this.",
    # "When you hug yourself, he/she will feel understood, appreciated, and loved. He/she has completed the task of conveying the signal.",
    # "He/she will try to let go of his control and will fully encourage you to follow your inner guidance. Whenever he/she appears, you can gently hug yourself.",
    # "Now, you can imagine him/her slowly merging with you. The two of you are originally one person. He/she is originally a part of your life. When a certain situation arises, he will stand up to express himself.",
    # "As long as you hug yourself gently, he will feel understood, supported, loved, and appreciated.",
    # "He/she will give back the leadership of life to you.",
    "Now, you can still look at the situation quietly, open your eyes, and return to the present.",
    "How do you feel now?",
    "continue",
    "Alright, try this in the future. If you encounter a situation that makes you feel uncomfortable, gently hug yourself like this. Then follow your inner feelings. ",
    "He/she just needs to be understood, comforted, loved, appreciated, hugged, or accompanied. ",
    "As long as he/she feels all this, his/her mission is complete, and he/she will give back the leadership to you, no longer interfering or affecting you.",
    "Congratulations on completing this awareness exercise, you did a great job!",
    "Done",
    "mask_getpic_from_word",
]

import openai
import requests

openai.api_key = 'sk-proj-Bue2ofTbTAvx2ExJvNGdT3BlbkFJqvLfVmmvjcveUaEpQoGS'

class OpenaiThread(QThread):
    signal_IsWaiting= pyqtSignal(int)

    def __init__(self):
        super().__init__()

        # 设置 OpenAI API 密钥

        # self.engine.startLoop(False)    # 使用非阻塞方式播放，方便在需要时中止

    def GetPic(self, keyWordlist, descretion):

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

    def run(self):
        while 1:
            # if self.txtValue != "":
            #     self.signal_IsSpeeking.emit(1)
            #     self.engine.say(self.txtValue)
            #     self.engine.runAndWait()
            #     self.txtValue = ""
            #     self.signal_IsSpeeking.emit(0)
            # else:
            pass
            time.sleep(0.01)

import pyttsx3
class SpeakerThread(QThread):
    signal_IsSpeeking = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.txtValue = "Hello! Nice to meet you."
        self.engine = pyttsx3.init()
        # self.engine.startLoop(False)    # 使用非阻塞方式播放，方便在需要时中止

    def stopSpeak(self):
        self.engine.stop()

    def SetTxtStr(self, strValue):
        self.txtValue = strValue

    def run(self):
        while 1:
            if self.txtValue != "":
                self.signal_IsSpeeking.emit(1)
                self.engine.say(self.txtValue)
                self.engine.runAndWait()
                self.txtValue = ""
                self.signal_IsSpeeking.emit(0)
            else:
                time.sleep(0.01)


class Main_Form(QtWidgets.QMainWindow, Ui_MainWindow):
    signal_TestControl = pyqtSignal(int)

    def __init__(self):
        super(Main_Form, self).__init__()
        self.setupUi(self)
        # self.setStyleSheet(qdarkstyle.load_stylesheet())

        self.set_background('background.png')

        # pixmap = QPixmap('background.png')  # 按指定路径找到图片
        # self.label_background.setPixmap(pixmap)  # 在label上显示图片
        # self.label_background.setScaledContents(True)  # 让图片自适应label大小

        self.speakerThread = SpeakerThread()  # 语音播放线程，用于播放语音
        self.speakerThread.signal_IsSpeeking.connect(self.On_IsSpeeking)
        self.speakerThread.start()

        self._openaiThread = OpenaiThread()  # openai 线程，用于调用openai
        self._openaiThread.signal_IsWaiting.connect(self.On_IsSpeeking)
        self._openaiThread.start()

        self.label_image.setText("")
        self.pushButton_skip.hide()
        self.textEdit.hide()
        self.label_input.hide()

        # self.actionDisplayWaveform.triggered.connect(self._Waveform.show)
        # self.actionRecoder.triggered.connect(self.On_actionRecoder)
        # self.actionexit.triggered.connect(self.close)

        self.pushButton_continue.clicked.connect(self.on_pushButtonClicked)
        self.pushButton_skip.clicked.connect(self.on_pushButtonClicked)
        # self.pushButton_OutputValue_Setup_2.clicked.connect(self.on_pushButtonClicked)
        # self.pushButton_output_rate_setup_2.clicked.connect(self.on_pushButtonClicked)
        # self.pushButtonZero.clicked.connect(self.on_pushButtonClicked)
        # self.pushButtonZero_2.clicked.connect(self.on_pushButtonClicked)
        #
        # self.checkBox_Channel00.stateChanged.connect(self.On_CheckBoxChanged)
        # self.checkBox_Channel01.stateChanged.connect(self.On_CheckBoxChanged)
        # self.checkBox_output_start.stateChanged.connect(self.On_CheckBoxChanged)
        # self.checkBox_output_start_2.stateChanged.connect(self.On_CheckBoxChanged)
        #
        # self.comboBox_Range00.currentIndexChanged.connect(self.On_comboBox_Change)
        # self.comboBox_Range01.currentIndexChanged.connect(self.On_comboBox_Change)
        #
        # self.comboBox_rate_mode.currentIndexChanged.connect(self.On_comboBox_Change)
        # self.comboBox_rate_mode_2.currentIndexChanged.connect(self.On_comboBox_Change)
        #
        # self.comboBox_Unit00.currentIndexChanged.connect(self.On_comboBox_Change)
        # self.comboBox_Unit01.currentIndexChanged.connect(self.On_comboBox_Change)
        # # 定时接收数据
        self.timer_Channel00 = QTimer()  # 初始化定时器
        self.timer_Channel00.timeout.connect(self.on_timeoutHandle)
        self.timer_Channel00.start(100)
        # self.s_nFlagUpdate = True
        # self._recDataBuff = ''
        #
        # self.s_nChannel00_Update_Enable = True
        # self.s_nChannel01_Update_Enable = True
        # self._IsRefresh00 = True  # 如果需要更新基础数据，则逐个发送数据
        # self._IsRefresh01 = True  # 如果需要更新基础数据，则逐个发送数据
        # self._FlagZeroEnable = False
        # self._IsRecoder = False  # 是否记录标识
        # self.counter_COMP = [0, 0]  # 周期更新正负压源
        # self.currentModeIndex = [0, 0]
        # self.lineEdit_output_rate.setDisabled(True)
        # self.lineEdit_output_rate_2.setDisabled(True)
        # self.IsUpdateMeasure = True  # 更新单位序列，只发送一次
        # self.currentUnitPres = ["", ""]  # 保存数据时的单位
        self._IsStart = 0
        self._currentIndex = 0
        self._IsSpeaking = 0  # 是否正在播放语音
        self._IsWaitingInput = 0  # 是否正在等待用户输入
        self._answerList = []  # 回复列表

        self.keyWordlist = []  # 用户输入关键字列表

    def On_IsSpeeking(self, status):
        self._IsSpeaking = status

    def set_background(self, image_path):
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap(image_path)))
        self.setPalette(palette)

    def on_timeoutHandle(self):  # reverse
        # 接收参数定义
        if self._IsStart:
            if self._IsSpeaking == 0 and self._IsWaitingInput == 0:
                if self._currentIndex < len(questionList) - 1:
                    quesstion = questionList[self._currentIndex]
                    if quesstion != "continue" and quesstion != "mask_getpic_from_word":
                        quesstionNext = questionList[self._currentIndex + 1]
                        if quesstionNext == "continue":  # 标识需要等待用户输入
                            self._IsWaitingInput = 1
                            self.pushButton_skip.hide()
                            self.pushButton_continue.show()
                            self.textEdit.show()
                            self.label_input.show()
                        else:
                            self.pushButton_skip.show()
                            self.pushButton_continue.hide()
                            self.textEdit.hide()
                            self.label_input.hide()

                        self.label_answer.setText(quesstion)
                        self.speakerThread.SetTxtStr(quesstion)
                        self._IsSpeaking = 1

                        quesstionNext_Next = questionList[self._currentIndex + 2]
                        if quesstionNext_Next == "mask_getpic_from_word":  # 标识需要等待openai返回数据
                            self._IsWaitingOpenaiRespone = 1
                            self._openaiThread.GetPic(self.keyWordlist, descretion)
                            self.keyWordlist.clear()
                            pass
                    self._currentIndex = self._currentIndex + 1
                    self.label_index.setText(str(self._currentIndex) + "/" + str(len(questionList)))

    def On_CheckBoxChanged(self, status):
        compnont = self.sender()
        if compnont == self.checkBox_Channel00:
            self.s_nChannel00_Update_Enable = compnont.isChecked()
            self._IsRefresh00 = compnont.isChecked()  # 如果需要更新基础数据，则逐个发送数据
        elif compnont == self.checkBox_Channel01:
            self.s_nChannel01_Update_Enable = compnont.isChecked()
            self._IsRefresh01 = compnont.isChecked()  # 如果需要更新基础数据，则逐个发送数据

    def on_pushButtonClicked(self):
        compnont = self.sender()
        if compnont == self.pushButton_continue:  # 启动排空
            self.pushButton_continue.setText("Comfirm")
            self._IsStart = 1  # 启动训练
            answerText = self.textEdit.toPlainText()
            if self._IsWaitingInput and answerText != "":
                self._IsWaitingInput = 0
                self._answerList.append(answerText)
                self.textEdit.clear()

        elif compnont == self.pushButton_skip:  # 跳过
            pass
            # self.speakerThread.stopSpeak()
            # self._IsSpeaking =0

    def On_comboBox_Change(self, index):
        compnont = self.sender()
        if compnont == self.comboBox_Range00:  # 设置量程
            if compnont.count() >= 2:  # 避免第一次添加就触发
                str = (":SOUR:PRES:RANG \"{}\"".format(compnont.currentText()))
                self._setupdialog.SendDataByUart(str.encode())
                time.sleep(0.01)
                self._IsRefresh00 = True  # 如果需要更新基础数据，则逐个发送数据
        elif compnont == self.comboBox_Range01:
            if compnont.count() >= 2:  # 避免第一次添加就触发
                str = (":SOUR2:PRES:RANG \"{}\"".format(compnont.currentText()))
                self._setupdialog.SendDataByUart(str.encode())
                time.sleep(0.01)
                self._IsRefresh01 = True  # 如果需要更新基础数据，则逐个发送数据

    def closeEvent(self, event):  # 函数名固定不可变
        sys.exit(0)  # 状态码


if __name__ == "__main__":
    app = QApplication(sys.argv)
    sys.exit(app.exec_())
