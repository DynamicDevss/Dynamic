import discord
from discord.ext import commands


class moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
            print('Moderation Cog is up')

    @commands.command()
    async def cog2test(self, ctx):
       await ctx.send('Cog 2 (moderation) is indeed up and working.')


    @commands.command()
    async def kick(self, ctx, member : discord.Member=None, *, reason=None, administrator=True):
        if member != None:
            await member.kick(reason=reason)
        else:
            await ctx.send('Please specify a user.')

    @commands.command
    async def ban(self, ctx, member : discord.Member=None, *, reason=None, administrator=True):
        if member != None:
            await member.ban(reason=reason)
        else:
            await ctx.send("Please specify a user.")

    @commands.command()
    async def clear(self, ctx, amount=5, administrator=True):
        await ctx.channel.purge(limit=amount)



def setup(client):
    client.add_cog(moderation(client))