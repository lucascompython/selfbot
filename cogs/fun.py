import discord, time
from discord import Intents
import json
from discord.ext import commands , tasks
import random
import string
import os
import time
import youtube_dl
from itertools import cycle
import datetime
from discord.utils import get
import asyncio
import requests
import sys
import math
import discord.ext
import pyfiglet
import aiohttp
import praw
from colorama import Fore


def RandomColor(): 
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor



with open(r"/home/lucas/Desktop/selfbot/cogs/other tokens/token1.txt", "r") as f:
    APP_ID = f.readlines()[0]

with open(r"/home/lucas/Desktop/selfbot/cogs/other tokens/token2.txt", "r") as f:
    APP_SECRET = f.readlines()[0]


class Fun(commands.Cog):
    """drena marada"""

    def __init__(self,client):
        self.client = client
        self.reddit = None
        if APP_ID and APP_SECRET:
            self.reddit = praw.Reddit(client_id=APP_ID, client_secret=APP_SECRET,
                                      user_agent="ESCRAVO DO LUCAS:%s:1.0" % APP_ID)


        self.regionals = {'a': '\N{REGIONAL INDICATOR SYMBOL LETTER A}', 'b': '\N{REGIONAL INDICATOR SYMBOL LETTER B}',
                          'c': '\N{REGIONAL INDICATOR SYMBOL LETTER C}',
                          'd': '\N{REGIONAL INDICATOR SYMBOL LETTER D}', 'e': '\N{REGIONAL INDICATOR SYMBOL LETTER E}',
                          'f': '\N{REGIONAL INDICATOR SYMBOL LETTER F}',
                          'g': '\N{REGIONAL INDICATOR SYMBOL LETTER G}', 'h': '\N{REGIONAL INDICATOR SYMBOL LETTER H}',
                          'i': '\N{REGIONAL INDICATOR SYMBOL LETTER I}',
                          'j': '\N{REGIONAL INDICATOR SYMBOL LETTER J}', 'k': '\N{REGIONAL INDICATOR SYMBOL LETTER K}',
                          'l': '\N{REGIONAL INDICATOR SYMBOL LETTER L}',
                          'm': '\N{REGIONAL INDICATOR SYMBOL LETTER M}', 'n': '\N{REGIONAL INDICATOR SYMBOL LETTER N}',
                          'o': '\N{REGIONAL INDICATOR SYMBOL LETTER O}',
                          'p': '\N{REGIONAL INDICATOR SYMBOL LETTER P}', 'q': '\N{REGIONAL INDICATOR SYMBOL LETTER Q}',
                          'r': '\N{REGIONAL INDICATOR SYMBOL LETTER R}',
                          's': '\N{REGIONAL INDICATOR SYMBOL LETTER S}', 't': '\N{REGIONAL INDICATOR SYMBOL LETTER T}',
                          'u': '\N{REGIONAL INDICATOR SYMBOL LETTER U}',
                          'v': '\N{REGIONAL INDICATOR SYMBOL LETTER V}', 'w': '\N{REGIONAL INDICATOR SYMBOL LETTER W}',
                          'x': '\N{REGIONAL INDICATOR SYMBOL LETTER X}',
                          'y': '\N{REGIONAL INDICATOR SYMBOL LETTER Y}', 'z': '\N{REGIONAL INDICATOR SYMBOL LETTER Z}',
                          '0': '0⃣', '1': '1⃣', '2': '2⃣', '3': '3⃣',
                          '4': '4⃣', '5': '5⃣', '6': '6⃣', '7': '7⃣', '8': '8⃣', '9': '9⃣', '!': '\u2757',
                          '?': '\u2753'}
       









    @commands.command(aliases=["memes"],help = "Memes que vem diretamento do r/memes do reddit.")
    async def meme(self, ctx):
        await ctx.message.delete()
        async with ctx.channel.typing():
            subreddit = self.reddit.subreddit("memes")
            all_subs = []

            top = subreddit.top(limit = 100)

            for submission in top:
                all_subs.append(submission)

            random_sub = random.choice(all_subs)

            name = random_sub.title
            url = random_sub.url

            em = discord.Embed(title = name)

            em.set_image(url = url)

        await ctx.send(embed= em)




    @commands.command()
    async def acorda(self, ctx, mbr : discord.Member, ch1 : discord.VoiceChannel, ch2 : discord.VoiceChannel, num = 10):
        await ctx.message.delete()
        #for members in ctx.author.voice.channel.members:
        queres = input("Queres utilizar o duplo acorda(necessita ter o L33T OtherBot no server)?[s/n]")
        if queres == 's':
            membro = input("Digita o membro(mençao): ")
            canal1 = input("Digita o canal 1(nao pode ter emojis): ")
            canal2 = input("Digita o canal 2(nao pode ter emojis): ")

            await ctx.send(f".acorda {membro} {canal1} {canal2} {num}")
            await ctx.send("SENTE O PODER DO DUPLO ACORDA MUAAHAHAHA!")
        else:
           print("OKOK!")

        await ctx.send(f"{mbr.mention} está a ser acordado com sucesso!")
        for i in range(0, num):
            await mbr.move_to(ch1)
            await asyncio.sleep(0.5)
            await mbr.move_to(ch2)




    @commands.command()
    async def dog(self,ctx): # b'\xfc'
        await ctx.message.delete()
        r = requests.get("https://dog.ceo/api/breeds/image/random").json()
        em = discord.Embed()
        em.set_image(url=str(r['message']))
        try:
            await ctx.send(embed=em)
        except:
            await ctx.send(str(r['message']))    

    @commands.command()
    async def fox(self,ctx): # b'\xfc'
        await ctx.message.delete()
        r = requests.get('https://randomfox.ca/floof/').json()
        em = discord.Embed(title="Random fox image", color=16202876)
        em.set_image(url=r["image"])
        try:
            await ctx.send(embed=em)
        except:
            await ctx.send(r['image'])    






    @commands.command()
    async def joke(self,ctx):  # b'\xfc'
        await ctx.message.delete()
        headers = {
            "Accept": "application/json"
        }
        async with aiohttp.ClientSession()as session:
            async with session.get("https://icanhazdadjoke.com", headers=headers) as req:
                r = await req.json()
        await ctx.send(r["joke"])








    @commands.command()
    async def tts(self, ctx, *, message): # b'\xfc'
        await ctx.message.delete()
        buff = await do_tts(message)
        await ctx.send(file=discord.File(buff, f"{message}.wav"))




    @commands.command()
    async def regional(self, ctx, *, msg):
        """Replace letters with regional indicator emojis"""
        await ctx.message.delete()
        msg = list(msg)
        regional_list = [self.regionals[x.lower()] if x.isalnum() or x in ["!", "?"] else x for x in msg]
        regional_output = '\u200b'.join(regional_list)
        await ctx.send(regional_output)




    @commands.Cog.listener()
    async def on_ready(self):
        await asyncio.sleep(1)
        print(f"{Fore.BLACK}Fun ready!" + Fore.RESET)

def setup(client):
    client.add_cog(Fun(client))
