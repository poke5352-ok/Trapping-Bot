
import discord
from discord.ext import commands


class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if (704489170759843870 in [y.id for y in message.author.roles]) or (704490013391323179 in [y.id for y in message.author.roles]) or message.author == self.bot.user:
            pass
        else:
            if "discord.gg/" in message.content:
                pass


def setup(bot):
    bot.add_cog(moderation(bot))