import discord
from discord.ext import commands
from discord.ext.commands import bot

client = commands.Bot(command_prefix = [">"]) # creating bot variable with prefixes

@client.event
async def on_ready():
    print('We have logged in as {0.user}'
    .format(client))
    await client.change_presence(status=discord.Status.online, activity = discord.Activity(type=discord.ActivityType.watching, name="your commands"))



@client.command()
async def about(ctx):
     await ctx.send('Hi! This is DynamicDevs first project! Dont expect much but hi')




client.run('OTAwNDQwNDQxMjM1ODQ1MjMx.YXBWgg.eSn7YAouWFj_ngOj6kYU22j1uHk')
