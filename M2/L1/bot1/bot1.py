import discord
from discord.ext import commands
import os
import random
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def meme(ctx):
    # Usar ruta absoluta de la carpeta donde está el script
    images_folder = os.path.abspath("D:/Kodland/Python Pro/M2/L1/bot1/images")

    # Obtener lista de imágenes
    imagenes = os.listdir(images_folder)
    img_name = random.choice(imagenes)

    # Enviar imagen
    with open(os.path.join(images_folder, img_name), 'rb') as f:
        picture = discord.File(f)

    await ctx.send(file=picture)

#evento que indica que el bot está listo
@bot.event
async def on_ready():
    print(f'Bot está listo como {bot.user}')

#Verificacion de TOKEN
load_dotenv('D:/Kodland/Python Pro/M2/L1/bot1/discord_token.env')
TOKEN = os.getenv('DISCORD_TOKEN')

if TOKEN is None:
    raise ValueError("No se encontró el token de Discord. Asegúrate de que existe el archivo .env con DISCORD_TOKEN")

bot.run(TOKEN)