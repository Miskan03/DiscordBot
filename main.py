import discord
from discord.ext import commands

client = commands.Bot(command_prefix="your perfix")#can be +,=,.,-...

@client.event
async def on_ready():
    print("+ Bot has started.")
        await client.change_presence(activity=discord.Game(name='DISCORD BOT RPC'))
    
##EMBED COMMAND
@client.command()
async def command(git):
    embed = discord.Embed(
        colour = discord.Colour.blue()#instead of blue you can use whatever color you want
    )

    embed.add_field(name = "***MISKAN***" , value = "***github/Miskan03***")
    await git.send(embed = embed)

##JUST COMMAND
@client.command()
async def command1(hub):
    await hub.send('Miskan')

##BOT TOKEN ALWAYS NEEDS TO BE ON END
client.run("YOUR TOKEN")
