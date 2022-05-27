from controlador.darDeBaja import darBaja
import telebot

API_TOKEN = ''

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "Hola soy el bot de windows con python!")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
# @bot.message_handler(commands=['placa']) 
def echo_message(message):
    responded = False
    print('incoming:'+message.text)
    if len(message.text) == 7:
        print('digito ultimo: ' + (str(message.text[6:7])))
        ultimo_digito = int(message.text[6:7])
        if ultimo_digito >= 0 and ultimo_digito <= 9:
            print('ultimo digito si es numero ' + str(ultimo_digito))
            # msg.body(darBaja(message))
            bot.reply_to(message, darBaja(message.text))
        else:
            # msg.body('No corresponde a una placa')
            bot.reply_to(message, darBaja(message.text))

        responded = True

    if len(message.text) == 6:
        print('digito ultimo: ' + (str(message.text[5:6])))
        # msg.body(darBaja(message))
        bot.reply_to(message, darBaja(message.text))
        responded = True

    if not responded:
        # msg.body('I only know about vehicle and motorcycle!')
        bot.reply_to(message, 'I only know about vehicle and motorcycle!')
    # bot.reply_to(message, message.text)




bot.infinity_polling()