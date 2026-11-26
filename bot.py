import os

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

LINKS = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("📢 Our Channel", url="https://t.me/+vRcZSVHv2rAzYTYx")],
        [InlineKeyboardButton("💬 Main Chat", url="https://t.me/+vHy2DjR6LZU0OTVh")],
        [InlineKeyboardButton("🔗 Shrike Lounge", url="https://t.me/+bOOdbK4vPU05N2Vh")],
    ]
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Welcome! Choose one of our links below:",
        reply_markup=LINKS,
    )


async def links(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Here are our links:",
        reply_markup=LINKS,
    )


def main() -> None:
    if not TOKEN:
        raise RuntimeError("Set the TELEGRAM_BOT_TOKEN environment variable first.")

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("links", links))
    app.run_polling()


if __name__ == "__main__":
    main()
