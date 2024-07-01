
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

CHANNEL_ACCESS_TOKEN = 'DHq7y7N2iFyBQ0jrBj+qZN0d4KShBhZw0Oim2MNCqmkKpP5KcFt+w7euIxzcgH4OLoPG4DWjwL7XwyHnztEqeN0CYXzqYZPTR1u8onCkc3gDOX7dP63onAB/riwOf4kFh/EtpuzzOQsxIGKFF6xCiwdB04t89/1O/w1cDnyilFU=' #ここに自分のトークンを入れて下さい

USER_ID = 'U7626caf1b032e3f9126d334f9e219405' #ここに自分のユーザーIDを入れて下さい

def send_message(text):
    line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

    try:
        line_bot_api.push_message(U'U7626caf1b032e3f9126d334f9e219405', TextSendMessage(text=text))
    except LineBotApiError as e:
        print(e.message)

if __name__ == "__main__":
        text = "こんにちわ" #入力された文字を送ります
        send_message(text)