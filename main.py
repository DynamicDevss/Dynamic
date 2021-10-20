import discord
from discord.ext import commands


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

client= commands.Bot(command_prefix = '<')

@client.command()
async def ping(ctx):
    await ctx.send('pong')

@client.command()
async def about(ctx):
     await ctx.send('Hi! This is DynamicDevs first project! Dont expect much but hi')


client = MyClient()
client.run('dontgetmytokenprick')