import discord
from discord.ext import commands


class music(commands.Cog):
    def __init__(self, client):
        slef.client = client

        @commands.Cog.listener()
        async def on_ready(self):
            print('Cog #1 is up')

        @commands.command()
        async def cog1test(self, ctx):
            await ctx.send('Cog 1 is indeed up and working.')




def setup(client):
    client.add_cog(music(client))