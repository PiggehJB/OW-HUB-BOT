import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents,
                   help_command=None, case_insensitive=True)


@bot.event
async def on_ready():
    print("main.py loaded")


async def load():
    extenstions = ['cogs.commands', 'cogs.welcome']
    if __name__ == "__main__":
        for ext in extenstions:
            await bot.load_extension(ext)


async def main():
    await load()
    await bot.start('')

asyncio.run(main())
