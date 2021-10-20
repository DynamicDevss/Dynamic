import discord
from discord.ext import commands
from discord.ext.commands import bot

client = commands.Bot(command_prefix = [">"]) # creating bot variable with prefixes

@client.event
async def on_ready():
    print('We have logged in as {0.user}'
    .format(client))
    await client.change_presence(status=discord.Status.online, activity = discord.Activity(type=discord.ActivityType.watching, name="your commands"))

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.notfound):
        await ctx.send ('Command not detected.')

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None, administrator=True):
    await member.kick(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None, administrator=True):
    await member.ban(reason=reason)


@client.command()
async def about(ctx):
     await ctx.send('Hi! This is DynamicDevs first project! Dont expect much but hi')




client.run('OTAwNDQwNDQxMjM1ODQ1MjMx.YXBWgg.eSn7YAouWFj_ngOj6kYU22j1uHk')
