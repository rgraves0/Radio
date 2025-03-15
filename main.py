import os
import telegram
from telegram.ext import Application, CommandHandler

RADIO_STATIONS = {
    "coolfm": "http://live3.iqstream.co.th:8000/coolfm",
    "virginhitz": "http://live3.iqstream.co.th:8000/virginhitz",
    "efm": "http://live3.iqstream.co.th:8000/efm"
}

async def start(update, context):
    await update.message.reply_text("မင်္ဂလာပါ။ ထိုင်းရေဒီယိုလိုင်းတွေ နားထောင်ချင်ရင် /radio နဲ့ နာမည်ထည့်ပါ (ဥပမာ: /radio coolfm)")

async def radio(update, context):
    if not context.args:
        await update.message.reply_text("ရေဒီယိုလိုင်းနာမည် ထည့်ပါ (coolfm, virginhitz, efm)")
        return
    station = context.args[0].lower()
    if station in RADIO_STATIONS:
        await update.message.reply_text(f"ဒီမှာ {station} အတွက် Streaming URL ပါ: {RADIO_STATIONS[station]}")
    else:
        await update.message.reply_text("ဒီလိုင်းမရှိပါ။ coolfm, virginhitz, efm ထဲက တစ်ခုကို ရွေးပါ။")

def main():
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    application = Application.builder().token(token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("radio", radio))

    print("Bot စတင်ပါပြီ!")
    application.run_polling()

if __name__ == "__main__":
    main()
