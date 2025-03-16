# main.py
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

RADIO_STATIONS = {
    "coolfm": "https://coolism-web.cdn.byteark.com:8443/coolism.mp3",      # COOL Fahrenheit 93
    "virginhitz": "https://rs3.hitzfm.in.th/hitz/icecast.audio",          # 95.5 Virgin Hitz
    "efm": "https://rs3.hitzfm.in.th/efm/icecast.audio",                  # EFM 94
    "greenwave": "https://greenwave.becteroradio.com/greenwave.mp3",      # Green Wave 106.5 FM
    "chillfm": "https://chill89.becteroradio.com/chill89.mp3",            # Chill FM 89
    "mcotnews": "https://radio.mcot.net/fm1005"                           # MCOT News FM 100.5
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    welcome_msg = (
        "မင်္ဂလာပါ။ ထိုင်းရေဒီယိုလိုင်းတွေ နားထောင်ချင်ရင် /radio နဲ့ နာမည်ထည့်ပါ\n"
        "ဥပမာ: `/radio coolfm`\n"
        "ရွေးချယ်စရာ: coolfm, virginhitz, efm, greenwave, chillfm, mcotnews"
    )
    await update.message.reply_text(welcome_msg, parse_mode="Markdown")

async def radio(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not context.args:
        await update.message.reply_text(
            "ရေဒီယိုလိုင်းနာမည် ထည့်ပါ\n"
            "ဥပမာ: `/radio coolfm`\n"
            "ရွေးချယ်စရာ: coolfm, virginhitz, efm, greenwave, chillfm, mcotnews",
            parse_mode="Markdown"
        )
        return

    station = context.args[0].lower()
    if station in RADIO_STATIONS:
        stream_url = RADIO_STATIONS[station]
        reply_msg = (
            f"🎵 {station.upper()} ရေဒီယိုလိုင်း 🎵\n"
            f"Streaming URL: {stream_url}\n"
            "ဒီ URL ကို သင့် media player (ဥပမာ VLC) မှာ ထည့်ပြီး နားထောင်နိုင်ပါတယ်။"
        )
        await update.message.reply_text(reply_msg)
    else:
        await update.message.reply_text(
            "ဒီလိုင်းမရှိပါ။\n"
            "ရွေးချယ်စရာ: coolfm, virginhitz, efm, greenwave, chillfm, mcotnews\n"
            "ဥပမာ: `/radio coolfm`",
            parse_mode="Markdown"
        )

def main() -> None:
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        print("Error: TELEGRAM_BOT_TOKEN ကို environment variable ထဲမှာ ထည့်ပါ။")
        return

    application = Application.builder().token(token).build()

    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("radio", radio))

    print("Bot စတင်ပါပြီ!")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
