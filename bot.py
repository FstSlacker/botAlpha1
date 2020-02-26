# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 20:37:53 2020

@author: Konstantin
"""
import telebot
token='1137283074:AAG-j7YVn-qDj5GYaFKzyFkWGesrVSFVT7E'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, 'aaaaaa')
bot.polling()
