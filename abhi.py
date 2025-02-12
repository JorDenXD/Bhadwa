import telebot
import requests

TOKEN = "8095096286:AAGtId-d51HL7ezrDnqffKeQ4WF9ONEMieI"
API_URL = "https://nggemini.tiiny.io/?prompt="

bot = telebot.TeleBot(TOKEN)

# Start Command
@bot.message_handler(commands=["start"])
def start(message):
    text = "👋 Welcome! Use the following commands:\n\n"
    text += "🔹 /ask <question> - Get AI-generated response\n"
    text += "🔹 /help - Get support\n"
    text += "🔹 /admin - Contact Admin\n"
    text += "🔹 Zinda Hi Hu Saale"
    bot.send_message(message.chat.id, text)

# Ask Command (Fetch from API)
@bot.message_handler(commands=["ask"])
def ask(message):
    query = message.text.replace("/ask", "").strip()
    if not query:
        bot.send_message(message.chat.id, "❌ Please enter a question after /ask")
        return

    response = requests.get(API_URL + query)
    bot.send_message(message.chat.id, "🤖 AI Response:\n" + response.text)

# Help Command
@bot.message_handler(commands=["help"])
def help_command(message):
    text = "Koi Bhi Dikkat Ho To Niche Click Crow👇"
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton("💬 Contact Developer", url="https://t.me/ItZ_Your_4Bhi"))
    bot.send_message(message.chat.id, text, reply_markup=keyboard)

# Admin Command
@bot.message_handler(commands=["admin"])
def admin(message):
    bot.send_message(message.chat.id, "👤 Admin: @Research_wings")

# Live Command (Show Bot Members Count)
#@bot.message_handler(commands=["live"])
"""
def live(bot):
    chat = bot.get_chat(chat_id)
    member_count = chat.members_count
    print(f"Total members in the group: {member_count}")
"""

# Run Bot
bot.polling()
