import discord
from discord.ext import commands
import os 

cogs = [
    "cogs.general",
    "cogs.co-owner",

]

client = commands.Bot(command_prefix=".")

for cog in cogs:
    try:
        client.load_extension(cog)
    except Exception as e:
        print(e)

@client.command()
@commands.has_any_role("Mod", "Admin", "Owner", "Co-Owner")
async def reload(ctx):
    """ Reload all extensions """
    for exten in cogs:
        try:
            client.reload_extension(exten)
        except Exception as e:
            print(e)
    await ctx.send("Reload Succesful")   


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000) }ms')    


@client.event
async def on_ready():
    print('Bot is Ready')








@client.command()
@commands.has_any_role("Mod", "Admin", "Owner", "Co-Owner")
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)







 

client.run(os.environ['token']) #os.environ['token']