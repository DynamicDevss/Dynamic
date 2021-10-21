import discord
import os
from discord.ext import commands



class helpCommand(commands.HelpCommand):

    def __init__(self):
        super().__init__()

    async def send_bot_help(self, mapping):
        return await super().send_bot_help(mapping)

    async def send_cog_help(self, cog):
        return await super().send_cog_help(cog)

    async def send_group_help(self, group):
        return await super().send_group_help(group)

    async def send_command_help(self, command):
        return await super().send_command_help(command)

client = commands.Bot(command_prefix='<', help_command=helpCommand())  # creating bot variable with prefixes

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'
    .format(client))
    await client.change_presence(status=discord.Status.online, activity = discord.Activity(type=discord.ActivityType.watching, name="anime"))

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

client = commands.Bot(command_prefix = '<', help_command=helpCommand()) # creating bot variable with prefixes

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('')


#for actual admin cmd use "administrator=True"
# TY!