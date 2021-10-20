import discord
from discord.ext import commands
from discord.ext.commands import bot


client = commands.Bot(command_prefix = [">"]) # creating bot variable with prefixes

@client.event()
async def on_ready():
    print('Logged on as {0}!'.format(self.user))
    await client.change_presence(status=discord.Status.online, activity = discord.Activity(type=discord.ActivityType.watching, name="your commands"))

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
client.run('OTAwNDQwNDQxMjM1ODQ1MjMx.YXBWgg.eSn7YAouWFj_ngOj6kYU22j1uHk')
