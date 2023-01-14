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
    await bot.start('MTA2Mzg2MTQxMDI5NzMwMzA2MA.Gx9ccO.x0xZUdyL8_OLOuqB6DGNKgCEoFLUbs6MnDOVw4')

asyncio.run(main())
