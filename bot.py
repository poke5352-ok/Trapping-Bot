import discord
from discord.ext import commands
import os 


client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print('Bot is Ready')




@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000) }ms')



@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)







 

client.run(os.environ['token'])