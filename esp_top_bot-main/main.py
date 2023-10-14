import os 
import random
import discord
from discord.ext import commands
from bot_logic import gen_pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sección como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a + b)

@bot.command()
async def sub(ctx, a: int, b: int):
    await ctx.send(a - b)

@bot.command()
async def mult(ctx, a: int, b: int):
    await ctx.send(a * b)

images = [
    "meme1.jpg",
    "meme2.jpg",
    "meme3.jpg"
]

imageani = [
    "ani1.jpg",
    "ani2.jpg"
]

@bot.command()
async def meme(ctx):
    img_name = random.choice(images)
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def memepet(ctx):
    img_name = random.choice(imageani)
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

bot.run("MTE1NTIwMTQ0NjcxMTY3NzAxOQ.GbC-V2.GBaaySRdXzNU5K-22jIZl3rD7VdLekCx_04nJg")
