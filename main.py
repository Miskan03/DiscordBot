import discord
from discord.ext import commands

client = commands.Bot(command_prefix="?")# discord bot perfix ('your perfix')

@client.event
async def on_ready():
    print("+ Bot has started.")
    
##EMBED COMMAND
@client.command()
async def hello(ctx):
    embed = discord.Embed(
        colour = discord.Colour.blue()##instead of blue you can use whatever color you want
    )

    embed.add_field(name = "***MISKAN***" , value = "***Hello welcome to server-name***")
    await ctx.send(embed = embed)

##JUST COMMAND
@client.command()
async def miskan(ctx):
    await ctx.send('Miskan')

##BOT TOKEN ALWAYS NEEDS TO BE ON END
client.run("")
