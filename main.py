import discord
from discord.ext import commands
from discord.ext.commands import bot


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

client= commands.Bot(command_prefix = '<')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def about(ctx):
     await ctx.send('Hi! This is DynamicDevs first project! Dont expect much but hi')

@bot.command()
async def delta(ctx, *, member: JoinDistanceConverter):
    is_new = member.delta.days < 100
    if is_new:
        await ctx.send("Hey you're pretty new!")
    else:
        await ctx.send("Hm you're not so new.")
@bot.command()
async def joined(ctx, *, member: discord.Member):
    await ctx.send('{0} joined on {0.joined_at}'.format(member))

client = MyClient()
client.run('dontgetmytokenprick')