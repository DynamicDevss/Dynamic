import discord
from discord.ext import commands


class utility(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
            print('Utility Cog is up')

    @commands.command(pass_context=True)
    async def nick(ctx, member: discord.Member, nick, self):
        await member.edit(nick=nick)
        await ctx.send(f'Nickname was changed for {member.mention} ')

def setup(client):
    client.add_cog(utility(client))



