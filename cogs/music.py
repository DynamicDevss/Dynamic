import discord
import os
from discord.ext import commands
import youtube_dl




def setup(client):
    client.add_cog(music(client))




class music(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send('Please join a voice channel first.')
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            ctx.voice_client.move_to(voice_channel)

    @commands.command()
    async def disconnect(self, ctx):
        await ctx.voice_client.dissconect()


    @commands.command()
    async def play(self, ctx, url):
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect-streamed 1 -reconnect-delay-max 5', 'options': '-vn'}
        YDL_OPTIONS = {'format':"bestaudio"}
        print('Options have been declared')
        vc: object = ctx.voice_client
        print('VC has been declared')

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            print('Download has started')
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            print('Music downloaded')
            vc.play('source')
            print('Music should be playing')

    @commands.command()
    async def pause(self, ctx):
        await ctx.voice_client.pause()
        await ctx.send('Music has been paused.')

    @commands.command()
    async def resume(self, ctx):
        await ctx.voice_client.resume()
        await ctx.send('Music has been resumed.')





    @commands.command()
    async def cog1test(self, ctx):
        ctx.send('Cog 1 (music) is indeed up and working.')
