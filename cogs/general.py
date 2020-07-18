import discord
from discord.ext import commands


class general(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.bot.latency * 1000) }ms') 

    async def presence_update(self):
        guild = self.bot.get_guild(704488514112192573)
        if guild:
            await self.bot.change_presence(activity=discord.Game(name=f"with {guild.member_count} users"))
            return
        

    @commands.Cog.listener()
    async def on_ready(self):
        await self.presence_update()

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await self.presence_update()

    @commands.Cog.listener()
    async def on_member_leave(self, member):
        await self.presence_update()


def setup(bot):
    bot.add_cog(general(bot))