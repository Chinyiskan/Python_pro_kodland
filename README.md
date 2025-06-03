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
6. [Plantillas Jinja2 en Flask](#-plantillas-jinja2-en-flask)
7. [Formularios HTML con Flask](#-formularios-html-con-flask)
8. [SQLAlchemy con Flask](#-sqlalchemy-con-flask)

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

[Volver al Índice](#-índice)  

---

## 🌐 Llamadas a APIs con requests  
> Explicación sobre cómo hacer peticiones HTTP en Python.  
[Volver al Índice](#-índice)  

### 📦 Instalación
```bash
pip install requests
```

### 🔥 Ejemplo de Uso

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

[Volver al Índice](#-índice)

---

## 🌐 Introducción a HTML y CSS  
> Antes de usar Flask, debemos entender cómo se estructura y se diseña una página web.
[Volver al Índice](#-índice)

### 🧱 ¿Qué es HTML?
HTML (HyperText Markup Language) es el lenguaje que usamos para **estructurar** el contenido de una página web.

Ejemplo de una estructura básica:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Mi Primera Página</title>
</head>
<body>
    <h1>Bienvenido a mi Web</h1>
    <p>Este es un párrafo de ejemplo.</p>
    <img src="imagen.jpg" alt="Una imagen">
</body>
</html>
```

### 🎨 ¿Qué es CSS?
CSS (Cascading Style Sheets) se usa para **dar estilo** a los elementos HTML.

```html
<style>
  body {
    background-color: #f0f8ff;
    font-family: Arial, sans-serif;
  }
  h1 {
    color: #663399;
  }
</style>
```

[Volver al Índice](#-índice)

---

## 🎨 Plantillas Jinja2 en Flask
> Cómo usar el motor de plantillas Jinja2 para crear páginas web dinámicas con Flask.
[Volver al Índice](#-índice)

### 📦 Instalación
Jinja2 viene incluido con Flask, así que no necesitas instalarlo por separado.

### 🔥 Sintaxis Básica de Jinja2

| Sintaxis | Descripción |
|----------|-------------|
| `{{ variable }}` | Muestra el valor de una variable |
| `{% if condición %}` | Estructuras de control (if, for, etc.) |
| `{# comentario #}` | Comentarios que no se mostrarán en el HTML |
| `{% extends 'base.html' %}` | Herencia de plantillas |
| `{% block nombre %}` | Bloques que pueden ser sobrescritos |

### 🛠️ Ejemplo de Uso

```python
# En Flask (app.py)
@app.route('/')
def index():
    nombre = "Usuario"
    items = ["Item 1", "Item 2", "Item 3"]
    return render_template('index.html', nombre=nombre, items=items)
```

```html
<!-- En la plantilla (index.html) -->
{% extends 'base.html' %}

{% block content %}
    <h1>¡Hola, {{ nombre }}!</h1>
    
    <ul>
    {% for item in items %}
        <li>{{ item }}</li>
    {% endfor %}
    </ul>
{% endblock %}
```

[Volver al Índice](#-índice)

---

## 📝 Formularios HTML con Flask
> Procesamiento de formularios web usando Flask.
[Volver al Índice](#-índice)

### 🔥 Conceptos Clave

| Concepto | Descripción |
|----------|-------------|
| `methods=['GET', 'POST']` | Especifica métodos permitidos en la ruta |
| `request.form` | Accede a datos enviados por POST |
| `request.args` | Accede a datos enviados por GET |
| `redirect()` | Redirecciona a otra página |

### 🛠️ Ejemplo de Formulario

```python
# En Flask
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        return f'¡Hola, {nombre}!'
    return render_template('form.html')
```

```html
<!-- form.html -->
<form method="POST" action="{{ url_for('form') }}">
    <input type="text" name="nombre" required>
    <button type="submit">Enviar</button>
</form>
```

[Volver al Índice](#-índice)

---

## 🗄️ SQLAlchemy con Flask
> ORM (Object-Relational Mapping) para trabajar con bases de datos en Flask.
[Volver al Índice](#-índice)

### 📦 Instalación
```bash
pip install flask-sqlalchemy
```

### 🔥 Configuración Básica

```python
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
```

### 📊 Definiendo Modelos

```python
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True)
```

### 🛠️ Operaciones Comunes

| Operación | Código |
|-----------|--------|
| Crear registro | `db.session.add(nuevo_usuario)` |
| Guardar cambios | `db.session.commit()` |
| Buscar todos | `Usuario.query.all()` |
| Buscar por ID | `Usuario.query.get(1)` |
| Filtrar | `Usuario.query.filter_by(nombre='Juan')` |
| Ordenar | `Usuario.query.order_by(Usuario.nombre)` |

### 📝 Ejemplo Completo

```python
# Crear
nuevo_usuario = Usuario(nombre='Juan', email='juan@ejemplo.com')
db.session.add(nuevo_usuario)
db.session.commit()

# Leer
usuarios = Usuario.query.all()
usuario = Usuario.query.get(1)

# Actualizar
usuario.nombre = 'Juan Carlos'
db.session.commit()

# Eliminar
db.session.delete(usuario)
db.session.commit()
```

[Volver al Índice](#-índice)

---

## 🎯 Ahora es tu turno

Con estas bases, ya puedes empezar a crear tus propias aplicaciones web con Flask. 🚀

Si tienes dudas, pregunta en la comunidad o revisa la documentación oficial. ¡Diviértete programando! 🎉
