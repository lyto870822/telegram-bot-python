# Telegram Bot con Python 🤖

Bot de Telegram creado con `python-telegram-bot` que responde comandos,
envia stickers y fotos, y muestra un menu interactivo.

## Instalacion

```bash
pip install -r requirements.txt
```

## Configuracion

1. Abre Telegram y busca [@BotFather](https://t.me/BotFather)
2. Escribe `/newbot` y sigue las instrucciones
3. Copia el token que te da BotFather
4. Pon el token en una variable de entorno:

```bash
export BOT_TOKEN="tu_token_aqui"
```

O edita `bot.py` y reemplaza `PON_TU_TOKEN_AQUI` con tu token.

## Ejecutar

```bash
python3 bot.py
```

## Comandos

- `/start` — Inicia el bot y muestra el menu interactivo
- `/help` — Muestra la lista de comandos
- `/sticker` — Recibe un sticker de ejemplo
- `/foto` — Recibe una foto de ejemplo

## Despliegue gratis

Sube este repo a GitHub y conectalo con [Render.com](https://render.com)
para tener tu bot funcionando 24/7 sin pagar nada.

---

Creado para el tutorial de YouTube. Suscribete para mas contenido! 🐍
