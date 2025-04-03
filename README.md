# 🤖 Introducción a discord.py

¡Hola chicos del curso de Python Pro! 👋

En este README encontrarán información básica para repasar los principales conceptos de las librerías que iremos estudiando durante el curso. No es un reemplazo de la documentación oficial, pero sí un buen punto de partida para comenzar rápido. 🚀

---

## 📦 Instalación

Antes de empezar, asegúrate de tener Python instalado en tu PC (preferiblemente 3.8 o superior).

Para instalar discord.py, usa este comando en la terminal:
```bash
pip install discord
```

---

## 🔥 Funciones Clave de discord.py

| Funcionalidad | Descripción |
|--------------|-------------|
| `commands.Bot` | Permite crear un bot con comandos personalizados. |
| `on_ready` | Evento que se ejecuta cuando el bot está listo. |
| `on_message` | Detecta y responde a mensajes enviados en un canal. |
| `on_member_join` | Se activa cuando un nuevo usuario entra al servidor. |
| `bot.command()` | Define comandos personalizados que los usuarios pueden ejecutar. |
| `discord.Embed` | Permite crear mensajes embellecidos con títulos, colores e imágenes. |
| `bot.run(TOKEN)` | Inicia el bot con el token de autenticación. |

---

## 🛠️ Creando un Bot Básico

1️⃣ Ve a [Discord Developer Portal](https://discord.com/developers/applications), crea una aplicación y un bot.
2️⃣ Copia el **TOKEN** del bot (guárdalo en un `.env`, nunca lo compartas).
3️⃣ Agrega el bot a un servidor con los permisos adecuados.

Ahora, un bot básico en `bot.py`:
```python
import discord
from discord.ext import commands
import os

# Definir prefijo y bot
bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f'✅ {bot.user} está listo para la acción!')

# Comando de ejemplo
@bot.command()
async def hola(ctx):
    await ctx.send("Hola! 👋")

# Iniciar el bot (usando variables de entorno)
bot.run(os.getenv("DISCORD_TOKEN"))
```

---

## 🛡️ Usando `dotenv` para Proteger el TOKEN del Bot

Para evitar exponer información sensible como el TOKEN del bot, usamos `dotenv`, que nos permite almacenar valores en un archivo `.env`. 🎭

### 1️⃣ Instalar `python-dotenv`
Ejecuta en la terminal:
```bash
pip install python-dotenv
```

### 2️⃣ Crear el archivo `.env`
En el directorio del proyecto, crea un archivo llamado `.env` y agrega:
```env
DISCORD_TOKEN=tu_super_secreto_token_aqui
```
🔹 **Recuerda**: Para evitar que este archivo se suba a GitHub, agrégalo al `.gitignore`:
```bash
echo "*.env" >> .gitignore
```

### 3️⃣ Modificar `bot.py` para Usar `dotenv`
```python
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv  # Importamos dotenv

# Cargar variables desde .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")  # Obtener el TOKEN del archivo .env

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f'✅ {bot.user} está listo para la acción!')

bot.run(TOKEN)  # Iniciar el bot
```

### 4️⃣ Verificar que Todo Funcione
Ejecuta el script:
```bash
python bot.py
```
Si todo está bien, deberías ver el mensaje ✅ en la consola sin exponer tu TOKEN en el código. 🎉

---

## ⚡ Eventos Importantes

Discord usa eventos para reaccionar a lo que ocurre en los servidores. Algunos esenciales:

```python
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return  # Evitar que el bot se responda a sí mismo
    
    if "ping" in message.content.lower():
        await message.channel.send("Pong! 🏓")

    await bot.process_commands(message)  # Permite que los comandos funcionen
```

```python
@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="general")
    if channel:
        await channel.send(f'Bienvenido, {member.mention}! 🎉')
```

---

## 🎮 Comandos Más Usados

| Comando | Descripción |
|---------|-------------|
| `!hola` | Saluda al usuario |
| `!ping` | Responde "Pong!" |
| `!info` | Muestra info del servidor |
| `!clear N` | Borra N mensajes del chat (requiere permisos) |

Ejemplo de comando con argumentos:
```python
@bot.command()
async def decir(ctx, *, mensaje):
    await ctx.send(mensaje)  # Repite el mensaje enviado
```

---

## 🛑 Consejos Importantes

🔹 **Nunca compartas tu TOKEN** (usa un `.env` o variables de entorno).
🔹 Usa `bot.process_commands(message)` en `on_message` para evitar conflictos con comandos.
🔹 Lee la documentación oficial: [discord.py Docs](https://discordpy.readthedocs.io/en/stable/)

---

## 🎯 Ahora es tu turno

Con estas bases, ya puedes empezar a crear tu propio bot y explorar nuevas funcionalidades. 🚀

Si tienes dudas, pregunta en la comunidad o revisa ejemplos online. ¡Diviértete programando! 🎉

