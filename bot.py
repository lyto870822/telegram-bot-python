#!/usr/bin/env python3
"""
Telegram Bot de ejemplo — Responde comandos, envia stickers, y muestra menu interactivo.
Creado para el tutorial de YouTube.
"""
import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# ── Configuracion ──
TOKEN = os.environ.get("BOT_TOKEN", "PON_TU_TOKEN_AQUI")
STICKER_ID = "CAACAgIAAxkBAA..."  # Reemplaza con tu sticker ID

# ── Comando /start ──
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    botones = [
        ["Precios", "Ayuda"],
        ["Contacto", "Sobre mi"],
    ]
    markup = ReplyKeyboardMarkup(botones, resize_keyboard=True)
    await update.message.reply_text(
        "Hola! Soy tu bot creado con Python!\nElige una opcion:",
        reply_markup=markup,
    )

# ── Comando /help ──
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Comandos disponibles:\n"
        "/start - Iniciar bot\n"
        "/help - Mostrar ayuda\n"
        "/sticker - Recibir un sticker\n"
        "/foto - Recibir una foto"
    )

# ── Comando /sticker ──
async def sticker(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_sticker(
        chat_id=update.effective_chat.id,
        sticker=STICKER_ID,
    )

# ── Comando /foto ──
async def foto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = "https://i.imgur.com/ejemplo.jpg"
    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=url,
        caption="Aqui tienes una foto!",
    )

# ── Manejador de mensajes de texto ──
async def manejar_mensaje(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text.lower()

    if texto == "precios":
        await update.message.reply_text("Los precios son:\nCurso Python: $100\nBot: Gratis!")
    elif texto == "ayuda":
        await help_command(update, context)
    elif texto == "contacto":
        await update.message.reply_text("Escribeme a: ejemplo@email.com")
    elif texto == "sobre mi":
        await update.message.reply_text("Soy un bot creado con python-telegram-bot!")
    else:
        await update.message.reply_text(f"Escribiste: {texto}")

# ── Main ──
def main():
    app = Application.builder().token(TOKEN).build()

    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("sticker", sticker))
    app.add_handler(CommandHandler("foto", foto))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, manejar_mensaje))

    print("Bot iniciado! Presiona Ctrl+C para detener.")
    app.run_polling()

if __name__ == "__main__":
    main()
