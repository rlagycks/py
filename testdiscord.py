import discord
from discord.ext import commands
 
app = commands.Bot(command_prefix='/',intents=discord.Intents.all())
 
@app.event
async def on_ready():
    print('Done')
    await app.change_presence(status=discord.Status.online, activity=None)

@app.command()
async def hello(ctx):
    await ctx.send('Hello I am Bot!')
    
app.run('MTA4ODEyNjc3Mjg2MTczOTEzOQ.GTK4Ir.1TPd-GnwMHhEM6xCkVuNXcBZrwOJIxMrgjdqbY')