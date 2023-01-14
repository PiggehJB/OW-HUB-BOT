import discord
from discord.ext import commands


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('commands.py loaded')

    @commands.command()
    async def verifyme(self, ctx):
        if ctx.channel.id == 1063852940282056824:
            embed = discord.Embed(
                title='Verification Successful! ✅',
                description=f'Congrats {ctx.author.mention} you have been verified. Thank you for joining the same and if you have any questions please feel free to message\
                    staff. You now have access to all basic channels and if you do not see them please restart discord. Thank you!',
                color=discord.colour.Color.from_rgb(244, 127, 255)
            )
            embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon)
            embed.set_footer(text='Thanks for joining!')
            embed.set_image(
                url='https://media.discordapp.net/attachments/1063963068645785670/1063963127869341756/verified_banner.png')
            await ctx.author.add.role()
            await ctx.message.add_reaction('✅')
            await ctx.author.send(embed=embed)
        else:
            await ctx.author.send('You need to use the verify <#1063852940282056824> channel')


async def setup(bot):
    await bot.add_cog(Commands(bot))
