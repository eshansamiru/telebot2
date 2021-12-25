import telebot
import time

bot_token = "5002572407:AAHnM0MzJvxFfxy_TPrvVUtv51EpdcsBndY"
bot = telebot.TeleBot(Token=bot_token)

@bot.message_handler(commands=["start"])


def short(url):
    return pyshorteners.Shotner().tinyurl.short(url)

def send_walcome(message):
    bot.reply_to(message, "Hello, welcome")
    
    @bot.message_handler(commands=["help"])
def send_walcome(message):
    bot.reply_to(message, "Read my description for the further help")
    
    @bot.message_handler(content types=["photo", "video", "audio", "document"])
    def file_sent(message):
        try:
            bot.send_message(message.chat.id, short(bot.get_file_url(message.document.file_id)))
        except AttributeError:
            try:
            bot.send_message(message.chat.id, short(bot.get_file_url(message.photo[0].file_id)))
        except AttributeError:
            try:
            bot.send_message(message.chat.id, short(bot.get_file_url(message.audio.file_id)))
        except AttributeError:
            try:
                try:
            bot.send_message(message.chat.id, short(bot.get_file_url(message.video.file_id)))
        except AttributeError:
            pass
            
    while True:
        try:
            bot polling()
except Exception:
    time.sleep(15)
    
