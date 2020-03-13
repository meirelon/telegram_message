# telegram_message
 small project to send a message to telegram via post request
 
## Deployment Directions
 ```
 git clone https://github.com/meirelon/telegram_message.git
 cd telegram_message
 pip install -r requirements.txt
 
 gcloud beta functions deploy send_tg_message --project=[YOUR PROJECT] --stage-bucket [YOUR BUCKET] --trigger-http --runtime=python37
 ```
 
## Python example

```
import requests

url = "https://us-central1-[YOUR PROJECT].cloudfunctions.net/send_tg_message"
params = {"token": [YOUR TELEGRAM BOT TOKEN], 
          "chat_id": [YOUR TELEGRAM CHAT ID], 
          "message": "testing out the cloud function :)"}


r = requests.post(url, json=params)
print(r.text)
```
