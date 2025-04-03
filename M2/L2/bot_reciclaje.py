import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Configuración del bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Opciones de información en un formato más organizado
RECYCLING_INFO = {
    "info_basica": {
        "title": "Información Básica",
        "content": "El reciclaje es un proceso en el que los materiales usados se convierten en nuevos productos para evitar el desperdicio.",
        "emoji": "ℹ️"
    },
    "separacion_desechos": {
        "title": "Separación de Desechos",
        "content": "Para reciclar correctamente, separa los desechos en orgánicos, plásticos, vidrios y papel/cartón.",
        "emoji": "🗑️"
    },
    "importancia_reciclaje": {
        "title": "Importancia del Reciclaje",
        "content": "El reciclaje ayuda a reducir la contaminación, ahorrar energía y conservar los recursos naturales.",
        "emoji": "♻️"
    },
    "cambio_climatico": {
        "title": "Impacto en el Cambio Climático",
        "content": "El reciclaje reduce las emisiones de gases de efecto invernadero al disminuir la necesidad de producir materiales nuevos.",
        "emoji": "🌡️"
    }
}

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="!ayuda para comenzar"))
    print(f'Bot conectado como {bot.user}')

@bot.command()
async def opciones(ctx):
    embed = discord.Embed(
        title="🌱 Temas sobre Reciclaje",
        description="Selecciona un tema usando `!info [tema]`",
        color=discord.Color.green()
    )
    
    for key, info in RECYCLING_INFO.items():
        embed.add_field(
            name=f"{info['emoji']} {info['title']}", 
            value=f"Usa: `!info {key}`",
            inline=False
        )
    
    await ctx.send(embed=embed)

@bot.command()
async def info(ctx, *, tema: str = None):
    if tema is None:
        await opciones(ctx)
        return

    tema = tema.lower().replace(" ", "_")
    if tema in RECYCLING_INFO:
        info = RECYCLING_INFO[tema]
        embed = discord.Embed(
            title=f"{info['emoji']} {info['title']}",
            description=info['content'],
            color=discord.Color.green()
        )
        await ctx.send(embed=embed)
    else:
        matches = [key for key in RECYCLING_INFO.keys() if tema in key]
        if matches:
            sugerencias = "\n".join([f"• `{RECYCLING_INFO[match]['title']}`" for match in matches])
            await ctx.send(f"❓ ¿Quizás quisiste decir?\n{sugerencias}")
        else:
            await ctx.send("❌ Tema no encontrado. Usa `!opciones` para ver los temas disponibles.")

@bot.command()
async def ayuda(ctx):
    embed = discord.Embed(
        title="📚 Comandos Disponibles",
        description="Aquí tienes una lista de todos los comandos",
        color=discord.Color.blue()
    )
    embed.add_field(name="!opciones", value="Muestra todos los temas disponibles", inline=False)
    embed.add_field(name="!info [tema]", value="Muestra información sobre un tema específico", inline=False)
    embed.add_field(name="!ayuda", value="Muestra este mensaje de ayuda", inline=False)
    
    await ctx.send(embed=embed)

# Cargar el token desde un archivo .env por seguridad
load_dotenv("D:/Kodland/Python Pro/M2/L2/discord_token.env")
TOKEN = os.getenv('DISCORD_TOKEN')

if TOKEN is None:
    raise ValueError("No se encontró el token de Discord. Asegúrate de que existe el archivo .env con DISCORD_TOKEN")

bot.run(TOKEN)