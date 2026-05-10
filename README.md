# Telegram Bot en Python 🤖

Bot de Telegram creado con `python-telegram-bot`. Responde a `/start`, envía stickers, muestra teclado personalizado y más.

## Instalacion

```bash
pip install -r requirements.txt
```

## Configuracion

1. Crea un bot con [@BotFather](https://t.me/BotFather) en Telegram
2. Copia el token que recibes
3. Asigna el token como variable de entorno:

```bash
export BOT_TOKEN="7234567890:AAE..."
```

O crea un archivo `.env`:

```
BOT_TOKEN=7234567890:AAE...
```

## Uso

```bash
python3 bot.py
```

## Comandos

- `/start` — Iniciar el bot
- `/sticker` — Recibir un sticker
- `/menu` — Mostrar teclado con botones
- `/help` — Ayuda

## Despliegue gratis

Sube este repositorio a [Render.com](https://render.com) como Web Service:
- Build Command: `pip install -r requirements.txt`
- Start Command: `python3 bot.py`
- Variable de entorno: `BOT_TOKEN`

## Requisitos

- Python 3.8+
- pip
