import discord
from discord.ext import commands
import youtube_dl

players = {}

class music(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
            print('Cog #1 is up')




   @client.command(pass_context=true)
   async def play(self, ctx, url)
   guild = ctx.message.guild
   voice_client = guild.voice_client
   player = await voice_client.create_ytdl_player(url)
   players[server.id] = player
   player.start

def setup(client):
    client.add_cog(music(client))