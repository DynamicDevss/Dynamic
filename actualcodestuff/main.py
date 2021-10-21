import discord
import os
from discord.ext import commands



client = commands.Bot(command_prefix='<')  # creating bot variable with prefixes


@client.event
async def on_ready():
    print('We have logged in as {0.user}'
    .format(client))
    await client.change_presence(status=discord.Status.online, activity = discord.Activity(type=discord.ActivityType.watching, name="anime"))

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send ('Command not detected.')


@client.command()
async def kick(ctx, member : discord.Member, *, reason=None, administrator=True):
    await member.kick(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None, administrator=True):
    await member.ban(reason=reason)

@client.command()
async def clear(ctx, amount=5, administrator=True):
    await ctx.channel.purge(limit=amount)



@client.command()
async def about(ctx):
     await ctx.send('Hi! This is DynamicDevs first project! Dont expect much but hi')

client = commands.Bot(command_prefix = '<',) # creating bot variable with prefixes

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('')


#for actual admin cmd use "administrator=True"
# TY!