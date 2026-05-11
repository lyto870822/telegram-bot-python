#!/usr/bin/env python3
"""
bot.py — Bot de Telegram completo con comandos, stickers y teclado.
Tutorial completo: https://github.com/lyto870822/telegram-bot-python

Uso:
  pip install -r requirements.txt
  python bot.py
"""
import asyncio
from telegram import ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters

TOKEN = "TU_TOKEN_AQUI"  # Reemplaza con el token de @BotFather

# ─── Comando /start ─────────────────────────────────
async def start(update, context):
    """Responde con mensaje de bienvenida y teclado."""
    botones = [["Hola", "Adios"]]
    teclado = ReplyKeyboardMarkup(botones, resize_keyboard=True)

    await update.message.reply_text(
        "Hola! Soy tu bot de Telegram creado con Python 🚀\n\n"
        "Usa los botones o escribe /help para ver comandos",
        reply_markup=teclado
    )

# ─── Comando /help ──────────────────────────────────
async def help_command(update, context):
    """Muestra los comandos disponibles."""
    await update.message.reply_text(
        "Comandos disponibles:\n"
        "/start - Inicia el bot\n"
        "/help - Muestra esta ayuda\n"
        "/sticker - Recibe un sticker\n"
        "Escribe 'Hola' o 'Adios' en el chat"
    )

# ─── Comando /sticker ───────────────────────────────
async def send_sticker(update, context):
    """Envia un sticker de ejemplo."""
    # Reemplaza con tu sticker_id de @Stickers o el que obtengas
    sticker_id = "CAACAgIAAxkBAAEBGQJmZ3QqP6St4T2JqR8HwQABCbcFAAQ"
    await update.message.reply_sticker(sticker_id)

# ─── Manejador de mensajes de texto ─────────────────
async def handle_message(update, context):
    """Responde a mensajes de texto."""
    text = update.message.text.lower()

    if "hola" in text:
        await update.message.reply_text("Hola! Como estas?")
    elif "adios" in text:
        await update.message.reply_text("Adios! Vuelve pronto")
    else:
        await update.message.reply_text(
            f"Dijiste: {text}\nUsa /help para ver comandos"
        )

# ─── Main ───────────────────────────────────────────
def main():
    app = Application.builder().token(TOKEN).build()

    # Registrar comandos
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("sticker", send_sticker))

    # Registrar mensajes de texto (no comandos)
    app.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND, handle_message
    ))

    print("Bot iniciado! Presiona Ctrl+C para detener")
    app.run_polling(allowed_updates=["message"])

if __name__ == "__main__":
    main()
