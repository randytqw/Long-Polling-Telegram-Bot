from bot import telegram_chatbot
import random

update_id = None

bot = telegram_chatbot("botConfig.cfg")

def generate_insult(name):
    insult_number = random.randint(0, 2)
    if insult_number == 0:
        return name + " you room temperature iq snail"
    elif insult_number == 1:
        return "Hey " + name + ", You know what the difference between your momma and a washing machine is? When I dump a load in a machine, the machine doesn't follow me around for three weeks."
    elif insult_number == 2:
        return name + " single from the womb, single till the tomb"

def make_reply(message):
    if message is not None:
        if message.startswith("/insult"):
            split_text = message.split()
            if len(split_text) != 2:
                return "invalid command"
            return generate_insult(split_text[1])
        return "invalid command"
    return None

while True:
    updates = bot.get_updates(offset = update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = item["message"]["text"]
            except:
                message = None
            sender = item["message"]["from"]["id"]
            chat = item["message"]["chat"]["id"]
            reply = make_reply(message)
            print(reply)
            bot.send_message(reply, chat)
