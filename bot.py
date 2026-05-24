import requests
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

print("TOKEN:", BOT_TOKEN)
print("CHAT:", CHAT_ID)

message = "🎉 اختبار إرسال من GitHub Actions"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

res = requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": message
})

print("STATUS:", res.status_code)
print("RESPONSE:", res.text)
