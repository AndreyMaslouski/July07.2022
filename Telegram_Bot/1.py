import telebot
from telebot import types


# Tokken = 5546376547:AAHgf4V3rsTgWPBk-6CKPvIOJLk_bQubzKg

token= '5546376547:AAHgf4V3rsTgWPBk-6CKPvIOJLk_bQubzKg'
bot = telebot.TeleBot(token)

def create_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    drink_btn = types.InlineKeyboardButton(text="Хочу пить", callback_data='1')
    eat_btn = types.InlineKeyboardButton(text="Хочу есть", callback_data='2')
    keyboard.add(drink_btn)
    keyboard.add(eat_btn)
    return keyboard

@bot.message_handler(commands=['start'])
def start_bot(message):
    keyboard=create_keyboard()
    bot.send_message(
        message.chat.id,
        "Добрый день! Выберите, что Вы хотите",
        reply_markup=keyboard
    )

if __name__=='__main__':
    bot.polling(none_stop=True)