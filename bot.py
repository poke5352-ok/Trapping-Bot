import discord
from discord.ext import commands
import os 
import json

cogs = [
    "cogs.general",
    "cogs.co-owner",
    "cogs.housing",
    "cogs.fossils"

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


    


@client.event
async def on_ready():
    try:
        with open('client_secret1.json', 'w') as file:
            json.dump(os.environ['jsonfile'], file)
    except:
        channel = self.bot.get_channel(722724050190991456)
            await channel.send('Failed')

    

    print('Bot is Ready')



 

client.run(os.environ['token']) #os.environ['token']