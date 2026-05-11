# Bot de Telegram en Python

Bot de Telegram completo con comandos, stickers y teclado personalizado. Tutorial para el canal de YouTube.

## Requisitos

- Python 3.8+
- Una cuenta de Telegram
- Un token de [@BotFather](https://t.me/BotFather)

## Instalación

```bash
pip install -r requirements.txt
```

## Uso

1. Edita `bot.py` y reemplaza `TU_TOKEN_AQUI` con tu token de BotFather
2. Ejecuta:

```bash
python bot.py
```

3. Abre Telegram, busca tu bot y escribe `/start`

## Comandos

- `/start` — Inicia el bot y muestra el teclado
- `/help` — Muestra los comandos disponibles
- `/sticker` — Envia un sticker de ejemplo

Escribe "Hola" o "Adios" y el bot te responderá.

## Despliegue en Render.com

1. Sube este repo a GitHub
2. Crea un Web Service en [Render.com](https://render.com)
3. Conecta tu repo
4. Start Command: `python bot.py`
5. Listo! Corre 24/7 gratis

## Licencia

MIT
