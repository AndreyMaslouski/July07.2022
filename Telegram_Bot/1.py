import telebot
from telebot import types

# Tokken = 5546376547:AAHgf4V3rsTgWPBk-6CKPvIOJLk_bQubzKg

token= '5546376547:AAHgf4V3rsTgWPBk-6CKPvIOJLk_bQubzKg'
bot = telebot.TeleBot(token)

def create_keyboard():
    keyboard = types.InlineKeyboardMarkup()