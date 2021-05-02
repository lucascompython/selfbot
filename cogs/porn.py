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
from colorama import Fore
import aiohttp




class Porn(commands.Cog):

    def __init__(self,client):
        self.client = client




    @commands.command()
    async def hentai(self,ctx): # b'\xfc'
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
        res = r.json()
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)   





    @commands.command()
    async def boobs(self,ctx): # b'\xfc'
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/boobs")
        res = r.json()
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


    @commands.command()
    async def slap(self,ctx, user: discord.Member): # b'\xfc'
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/slap")
        res = r.json()
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)



    @commands.command()
    async def hug(self,ctx, user: discord.Member): # b'\xfc'
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/hug")
        res = r.json()
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)













    @commands.Cog.listener()
    async def on_ready(self):
        await asyncio.sleep(1)
        print(f"{Fore.RED}Porn ready!" + Fore.RESET)


def setup(client):
    client.add_cog(Porn(client))
