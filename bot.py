#!/usr/bin/env python3
"""Create a complete Telegram bot using python-telegram-bot library."""

import os
from telegram.ext import Application, CommandHandler
from telegram import ReplyKeyboardMarkup

TOKEN = os.environ.get("BOT_TOKEN", "AQUI_TU_TOKEN")

# ── Sticker IDs (example — replace with real ones) ──
STICKER_ID = "CAACAgIAAxkBAA..."

# ── Commands ──

async def start(update, context):
    """Handle /start command."""
    await update.message.reply_text(
        "Hola! Soy un bot de Telegram creado con Python. "
        "Usa /start para verme, /sticker para un sticker, "
        "/menu para el teclado, /help para ayuda.",
    )

async def sticker(update, context):
    """Send a sticker."""
    await update.message.reply_sticker(STICKER_ID)

async def menu(update, context):
    """Show custom keyboard."""
    botones = [
        ["Ver Precio", "Ayuda"],
        ["Contacto", "Info"],
    ]
    markup = ReplyKeyboardMarkup(botones, resize_keyboard=True)
    await update.message.reply_text(
        "Elige una opcion:",
        reply_markup=markup,
    )

async def help_command(update, context):
    """Show help."""
    await update.message.reply_text(
        "Comandos disponibles:\n"
        "/start - Iniciar\n"
        "/sticker - Recibir un sticker\n"
        "/menu - Mostrar teclado\n"
        "/help - Esta ayuda"
    )

# ── Main ──

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("sticker", sticker))
    app.add_handler(CommandHandler("menu", menu))
    app.add_handler(CommandHandler("help", help_command))

    print("Bot iniciado. Presiona Ctrl+C para detener.")
    app.run_polling(allowed_updates=["message"])

if __name__ == "__main__":
    main()
