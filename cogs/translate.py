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
from googletrans import Translator
import typing as t

class Translate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot





    @commands.command()
    async def translate(self, ctx, destination: t.Optional[str], *, msg):
        if destination == None:
            destination = "pt"
        trans = Translator()
        t =trans.translate(msg,dest=destination)
        embed = discord.Embed(title="Tradutor")
        embed.add_field(name=f"Original ({t.src})", value=t.origin, inline=False)
        embed.add_field(name=f"Traduzido para {destination}", value=t.text)
        await ctx.send(embed=embed)
        print(f"{t.origin} -> {t.text}")

        #await ctx.send(result.text)



    @commands.Cog.listener()
    async def on_ready(self):
        await asyncio.sleep(1)
        print(f"{Fore.MAGENTA}Translate ready!" + Fore.RESET)



def setup(bot):
    bot.add_cog(Translate(bot))