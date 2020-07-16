import discord
from discord.ext import commands


class housing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_any_role("Admin", "Mod", "Co-Owner", "Owner", "Head-Co")
    async def eventstart(self, ctx):
        channel = self.bot.get_channel(705158446693089310)
        await channel.send('@everyone House is Up! Join now /visit Miniavocado!')
        

def setup(bot):
    bot.add_cog(housing(bot))