import discord
from discord.ext import commands


class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('welcome.py loaded')


async def setup(bot):
    await bot.add_cog(Welcome(bot))
