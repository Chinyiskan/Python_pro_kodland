import discord
from discord.ext import commands
import os
import json
from dotenv import load_dotenv
from news_api import NewsAPIWrapper  # módulo previamente creado
import datetime

# Cargar variables de entorno
load_dotenv("D:/Kodland/Python Pro/M2/L2/discord_token.env")
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
NEWS_API_KEY = os.getenv('NEWS_API_KEY')

if DISCORD_TOKEN is None:
    raise ValueError("No se encontró el token de Discord en el archivo .env")
if NEWS_API_KEY is None:
    raise ValueError("No se encontró la API key de NewsAPI en el archivo .env")

# Cargar información de reciclaje desde el archivo JSON
with open("recycling_info.json", "r", encoding="utf-8") as f:
    RECYCLING_INFO = json.load(f)

# Configuración del bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

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
        info_data = RECYCLING_INFO[tema]
        embed = discord.Embed(
            title=f"{info_data['emoji']} {info_data['title']}",
            description=info_data['content'],
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

# Instanciar el wrapper de NewsAPI
news_api = NewsAPIWrapper(api_key=NEWS_API_KEY)

@bot.command()
async def noticias(ctx, *, categoria: str = None):
    if categoria is None:
        categorias_disponibles = "\n".join([f"• `{cat.replace('_', ' ')}`" for cat in news_api.categories.keys()])
        await ctx.send(f"📰 **Categorías de noticias disponibles:**\n{categorias_disponibles}\n\nUsa: `!noticias [categoria]`")
        return

    categoria = categoria.lower().replace(" ", "_")
    if categoria not in news_api.categories:
        await ctx.send("❌ Categoría no válida. Usa `!noticias` para ver las categorías disponibles.")
        return

    try:
        noticias_data = news_api.get_news(categoria)
        if noticias_data['totalResults'] > 0:
            embed = discord.Embed(
                title=f"📰 Noticias sobre {categoria.replace('_', ' ').title()}",
                description="Últimas noticias relevantes",
                color=discord.Color.blue()
            )
            for articulo in noticias_data['articles']:
                titulo = articulo['title']
                url = articulo['url']
                descripcion = articulo['description'] or "Sin descripción disponible"
                
                if len(descripcion) > 200:
                    descripcion = descripcion[:197] + "..."
    
                embed.add_field(
                    name=titulo,
                    value=f"{descripcion}\n[Leer más]({url})",
                    inline=False
                )
    
            await ctx.send(embed=embed)
        else:
            await ctx.send("❌ No se encontraron noticias para esta categoría.")
    except Exception as e:
        await ctx.send("❌ Ocurrió un error al buscar las noticias. Por favor, intenta más tarde.")
        print(f"Error en comando noticias: {e}")

@bot.command()
async def ayuda(ctx):
    embed = discord.Embed(
        title="📚 Comandos Disponibles",
        description="Lista de comandos",
        color=discord.Color.blue()
    )
    embed.add_field(name="!opciones", value="Muestra todos los temas disponibles", inline=False)
    embed.add_field(name="!info [tema]", value="Muestra información sobre un tema específico", inline=False)
    embed.add_field(name="!noticias [categoria]", value="Muestra noticias recientes sobre medioambiente, cambio climático o reciclaje", inline=False)
    embed.add_field(name="!ayuda", value="Muestra este mensaje de ayuda", inline=False)
    
    await ctx.send(embed=embed)

bot.run(DISCORD_TOKEN)
