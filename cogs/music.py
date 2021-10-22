import discord
import os
from discord.ext import commands

def setup(client):
    client.add_cog(music(client))

players = {}

class music(commands.Cog):
    def __init__(self, client):
        self.client = client

   
    @commands.command()
    async def cog1test(self, ctx):
        ctx.send('Cog 1 () is indeed up and working.')


