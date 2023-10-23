import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user.name}")

@bot.command()
async def ping(ctx):
    latency = round(bot.latency * 1000)  # Convert latency to milliseconds
    await ctx.send(f'Pong! Latency is {latency}ms')

# Replace "YOUR_BOT_TOKEN_HERE" with your actual bot token
bot.run("MTE2MjUzNjgwMzc1NzIwNzU4NA.Gr-M-7.JcSVsjOl-jD8fp-QlzKWkEpOzKAfqbYL57nN84")