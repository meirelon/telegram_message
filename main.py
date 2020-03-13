import telegram
import requests

def send_tg_message(request):
    if request.method == "POST":
        try:
            r = request.get_json()
            token = r["token"]
            chat_id = r["chat_id"]
            message = r["message"]

            bot = telegram.Bot(token=token)
            bot.sendMessage(chat_id=chat_id, text=message)
            return "True"
        except Exception as e:
            return e
