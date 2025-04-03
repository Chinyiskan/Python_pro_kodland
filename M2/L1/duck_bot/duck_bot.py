import discord
from discord.ext import commands
import requests
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configurar el bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

# Evento que se ejecuta cuando el bot está listo
@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

# Ejecutar el bot
load_dotenv('D:/Kodland/Python Pro/M2/L1/duck_bot/discord_token.env')
TOKEN = os.getenv('DISCORD_TOKEN')

if TOKEN is None:
    raise ValueError("No se encontró el token de Discord. Asegúrate de que existe el archivo .env con DISCORD_TOKEN")

bot.run(TOKEN)