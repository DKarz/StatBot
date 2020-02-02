import telebot
import constants
import function as func


bot = telebot.TeleBot(constants.token)

keybordFlag = True

mode1 = [False, False, False]
mode2 = [False, False, False]
mode3 = [False]

def keyboard(msg_id):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row("Chi-square test for 2 samples")
    user_markup.row("Chi-square test for 1 samples")
    user_markup.row("Standard deviation")
    bot.send_message(msg_id, "...", reply_markup=user_markup)

@bot.message_handler(commands=["start"])
def hello(msg):
    global mode1
    global mode2
    global mode3
    mode1 = [False, False, False]
    mode2 = [False, False, False]
    mode3 = [False]
    keyboard(msg.chat.id)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    # if keybordFlag:
    #     keyboard(message.chat.id)
    if message.text == "Chi-square test for 2 samples":
        mode1[0] = True
        bot.send_message(message.chat.id, "Enter alpha:", reply_markup=telebot.types.ReplyKeyboardRemove())
    elif message.text == "Chi-square test for 1 samples":
        mode2[0] = True
        bot.send_message(message.chat.id, "Enter Observed and Expected:", reply_markup=telebot.types.ReplyKeyboardRemove())

    elif message.text == "Standard deviation":
        bot.send_message(message.chat.id, "Enter data", reply_markup=telebot.types.ReplyKeyboardRemove())
        mode3[0] = True
    elif mode1[0]:
        if mode1[1] == False:
            if message.text.isdigit() == False:
                mode1[0],mode1[1],mode1[2] = False, False, False
                bot.send_message(message.chat.id, "Error")
                keyboard(message.chat.id)
            else:
                func.alpha = int(message.text)
                bot.send_message(message.chat.id, "Enter table")
                mode1[1] = True
        else:
            mat1 = message.text.split("\n")
            mat = []
            for line in mat1:
                line = line.split(" ")
                for i in range (len(line)):
                    line[i] = float(line[i])
                mat.append(line)

            mode1[0], mode1[1], mode1[2] = False, False, False
            txt = func.calc(func.alpha, len(mat), mat)
            bot.send_message(message.chat.id, txt)

            keyboard(message.chat.id)
    elif mode2[0]:
        try:
            OE = message.text.split("\n")
            O = [float(i) for i in OE[0].split(" ")]
            E = [float(i) for i in OE[1].split(" ")]
            print(O, E)
            txt = func.chi1(O,E)
            mode2[0] = False
            bot.send_message(message.chat.id, txt)
        except:
            bot.send_message(message.chat.id, "Error")

        keyboard(message.chat.id)
    elif mode3[0]:
        try:
            data = [float(num) for num in message.text.split(" ")]
            x_bar = sum(data)/len(data)
            s2 = sum([(xi - x_bar)**2 for xi in data])/(len(data)-1)
            txt = "s^2 = " + str(s2)
            txt += "\ns = " + str(s2**0.5)
            bot.send_message(message.chat.id, txt)
        except:
            bot.send_message(message.chat.id, "Error")
        keyboard(message.chat.id)










bot.polling(none_stop=True, interval=0)