import os
from telegram.ext import Application, CommandHandler
from py_tgcalls import PyTgCalls, StreamType, idle
from py_tgcalls.types.input_stream import AudioPiped

RADIO_STATIONS = {
    "coolfm": "http://live3.iqstream.co.th:8000/coolfm",
    "virginhitz": "http://live3.iqstream.co.th:8000/virginhitz",
    "efm": "http://live3.iqstream.co.th:8000/efm"
}

token = os.getenv("TELEGRAM_BOT_TOKEN")
application = Application.builder().token(token).build()
pytgcalls = PyTgCalls(application)

async def start(update, context):
    await update.message.reply_text("မင်္ဂလာပါ။ ထိုင်းရေဒီယိုလိုင်းတွေ နားထောင်ချင်ရင် Group ထဲမှာ /radio နဲ့ နာမည်ထည့်ပါ (ဥပမာ: /radio coolfm)")

async def radio(update, context):
    if not context.args:
        await update.message.reply_text("ရေဒီယိုလိုင်းနာမည် ထည့်ပါ (coolfm, virginhitz, efm)")
        return
    station = context.args[0].lower()
    if station not in RADIO_STATIONS:
        await update.message.reply_text("ဒီလိုင်းမရှိပါ။ coolfm, virginhitz, efm ထဲက တစ်ခုကို ရွေးပါ။")
        return

    chat_id = update.effective_chat.id
    try:
        await pytgcalls.join_group_call(
            chat_id,
            AudioPiped(RADIO_STATIONS[station]),
            stream_type=StreamType().pulse_stream
        )
        await update.message.reply_text(f"{station} ကို ဖွင့်လိုက်ပါပြီ။ Group ထဲမှာ နားထောင်လို့ရပါပြီ။")
    except Exception as e:
        await update.message.reply_text(f"ဖွင့်မရပါ: {str(e)}")

def main():
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("radio", radio))
    application.run_polling()
    idle()

if __name__ == "__main__":
    main()
