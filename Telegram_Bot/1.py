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

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    keyboard = create_keyboard()
    if call.message:
        if call.data=='1':
            img = open('water','rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Картинка воды",
                reply_markup=keyboard)
            img.close()
        if call.data=='2':
            img = open('eat.jpg','rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Картинка еды",
                reply_markup=keyboard)
            img.close()
        if call.data=='3':
            img = open('vegetables.jpg','rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Картинка овощей",
                reply_markup=keyboard)
            img.close()
        if call.data=='4':
            img = open('Hochy Gulyat.jpg','rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Хочу гулять",
                reply_markup=keyboard)
            img.close()
        if call.data=='5':
            img = open('hochy spat.jpeg','rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Хочу спать",
                reply_markup=keyboard)
            img.close()
        if call.data == '6':
            img = open('Hochu shutky.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Хочу шутку",
                reply_markup=keyboard)
            img.close()

if __name__=="__main__":
    bot.polling(none_stop=True)