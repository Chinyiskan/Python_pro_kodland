# 📘 Curso Python Pro - README General

¡Hola chicos del curso de Python Pro! 👋

En este README encontrarán información básica para repasar los principales conceptos de las librerías que iremos estudiando durante el curso. No es un reemplazo de la documentación oficial, pero sí un buen punto de partida para comenzar rápido. 🚀

---

## 📌 Índice  
1. [Introducción a discord.py](#-introducción-a-discordpy)  
2. [Uso de dotenv para Tokens](#-uso-de-dotenv-para-tokens)  
3. [Llamadas a APIs con requests](#-llamadas-a-apis-con-requests)  
4. [Gestión de Git y GitHub](#-gestión-de-git-y-github)  
5. [Introducción a HTML y CSS](#-introducción-a-html-y-css)  

---

## 🤖 Introducción a discord.py  
> Explicación sobre la librería `discord.py`, cómo crear un bot y comandos básicos.  
[Volver al Índice](#-índice)  

### 📦 Instalación
Antes de empezar, asegúrate de tener Python instalado en tu PC (preferiblemente 3.8 o superior).

Para instalar discord.py, usa este comando en la terminal:
```bash
pip install discord
```

### 🔥 Funciones Clave de discord.py

| Funcionalidad | Descripción |
|--------------|-------------|
| `commands.Bot` | Permite crear un bot con comandos personalizados. |
| `on_ready` | Evento que se ejecuta cuando el bot está listo. |
| `on_message` | Detecta y responde a mensajes enviados en un canal. |
| `on_member_join` | Se activa cuando un nuevo usuario entra al servidor. |
| `bot.command()` | Define comandos personalizados que los usuarios pueden ejecutar. |
| `discord.Embed` | Permite crear mensajes embellecidos con títulos, colores e imágenes. |
| `bot.run(TOKEN)` | Inicia el bot con el token de autenticación. |

### 🛠️ Creando un Bot Básico

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

[Volver al Índice](#-índice)  

---

## 🔒 Uso de dotenv para Tokens  
> Cómo ocultar información sensible usando `.env`.  
[Volver al Índice](#-índice)  

### 🛑 Protegiendo el TOKEN con dotenv

Para evitar exponer información sensible como el TOKEN del bot, usamos `python-dotenv`.

1️⃣ Instalar dotenv:
```bash
pip install python-dotenv
```

2️⃣ Crear un archivo `.env` y guardar el TOKEN:
```env
DISCORD_TOKEN=tu_token_aqui
```

3️⃣ Modificar el código para leerlo desde el `.env`:
```python
from dotenv import load_dotenv
import os

load_dotenv()  # Carga las variables del .env
TOKEN = os.getenv("DISCORD_TOKEN")
```

4️⃣ Añadir `.env` al `.gitignore` para que no se suba a GitHub:
```gitignore
*.env
```

🔹 **Nunca compartas tu TOKEN**, usa `.env` o variables de entorno.  
[Volver al Índice](#-índice)  

---

## 🌐 Llamadas a APIs con requests  
> Explicación sobre cómo hacer peticiones HTTP en Python.  
[Volver al Índice](#-índice)  

Ejemplo de bot que obtiene imágenes aleatorias de gatos usando `requests`:
```python
import requests

@bot.command()
async def gato(ctx):
    response = requests.get("https://api.thecatapi.com/v1/images/search")
    if response.status_code == 200:
        data = response.json()
        await ctx.send(data[0]['url'])
    else:
        await ctx.send("No pude obtener una imagen 😿")
```

[Volver al Índice](#-índice)  

---

## 🛠 Gestión de Git y GitHub  
> Cómo trabajar con control de versiones para proyectos colaborativos.  
[Volver al Índice](#-índice)  

### 📌 Comandos básicos

```bash
git init  # Inicializa un repositorio
git add .  # Añadir cambios
git commit -m "Mensaje"  # Guardar cambios
git push origin main  # Subir al repositorio remoto
```

🔹 **Recuerda:** Usa `.gitignore` para evitar subir archivos sensibles.  
 
---

## 🎯 Ahora es tu turno

Con estas bases, ya puedes empezar a crear tu propio bot y explorar nuevas funcionalidades. 🚀

Si tienes dudas, pregunta en la comunidad o revisa ejemplos online. ¡Diviértete programando! 🎉

---

## 🌐 Introducción a HTML y CSS  
> Antes de usar Flask, debemos entender cómo se estructura y se diseña una página web. Aquí va una introducción muy básica.  
[Volver al Índice](#-índice)

### 🧱 ¿Qué es HTML?
HTML (HyperText Markup Language) es el lenguaje que usamos para **estructurar** el contenido de una página web.

Ejemplo de una estructura básica:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Página de Gatos</title>
</head>
<body>
    <h1>Bienvenido a la Web de Gatitos 🐱</h1>
    <p>Estos son algunos gatos muy adorables:</p>
    <img src="https://placekitten.com/300/200" alt="Gato lindo">
</body>
</html>
```

### 🎨 ¿Qué es CSS?
CSS (Cascading Style Sheets) se usa para **dar estilo** a los elementos HTML: colores, tamaños, márgenes, etc.

Ejemplo de reglas CSS básicas:
```html
<style>
  body {
    background-color: #f0f8ff;
    font-family: Arial, sans-serif;
    text-align: center;
  }
  h1 {
    color: #663399;
  }
  img {
    border-radius: 10px;
    box-shadow: 0 0 10px gray;
  }
</style>
```

### 🐾 Resultado Final
Una página HTML + CSS simple de gatos:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Gatitos Web</title>
    <style>
        body {
            background-color: #fce4ec;
            font-family: sans-serif;
            text-align: center;
        }
        h1 {
            color: #e91e63;
        }
        img {
            width: 300px;
            border-radius: 15px;
        }
    </style>
</head>
<body>
    <h1>🐱 Galería de Gatitos</h1>
    <p>¡Mira qué lindos!</p>
    <img src="https://placekitten.com/300/200" alt="gatito">
</body>
</html>
```

Así empezamos a entender cómo se construyen las páginas web, ¡para luego conectarlas con Python y Flask! 🚀

[Volver al Índice](#-índice)

