import discord
from discord.ext import commands
import gspread
from oauth2client.service_account import ServiceAccountCredentials


class fossils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    
    async def fossilcheck(self, ctx, name):
        scope = ['https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('bot-data/client_secret.json', scope)
        client = gspread.authorize(creds)
        sheet = client.open("Fossils & Win Spread Sheet").sheet1
        name = name.lower()
        try:
            cell = sheet.find(name)

            val = sheet.cell(cell.row, cell.col+1).value
            
            await ctx.send(name + " has " + val + " fossils.")
        except:
            await ctx.send(name + " has " + "0" + " fossils.")
    @commands.command()
    @commands.has_any_role("Admin", "Mod", "Co-Owner", "Owner", "Head-Co")
    async def fossiladd(self, ctx, name, add):
        scope = ['https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('bot-data/client_secret.json', scope)
        client = gspread.authorize(creds)
        sheet = client.open("Fossils & Win Spread Sheet").sheet1
        name = name.lower()
        try:
            
            cell = sheet.find(name)


            val = sheet.cell(cell.row, cell.col+1).value

            sheet.update_cell(cell.row, cell.col+1, int(val)+int(add))

            await ctx.send("Fossils added.")
        except:
            
                list = sheet.col_values(1)
                listlen = len(list)
                sheet.update_cell(listlen+1, 1, name)
                sheet.update_cell(listlen+1, 2, 0+int(add))

            
                

        
def setup(bot):
    bot.add_cog(fossils(bot))