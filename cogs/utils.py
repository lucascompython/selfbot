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








class Utils(commands.Cog):
    """drena marada"""

    def __init__(self,client):
        self.client = client















    @commands.command(aliases=['markasread', 'ack'])
    async def read(self, ctx): # b'\xfc'
        await ctx.message.delete()
        for guild in self.client.guilds:
            await guild.ack()















    @commands.Cog.listener()
    async def on_ready(self):
        await asyncio.sleep(1)
        print(f"{Fore.GREEN}Utils ready!" + Fore.RESET)

def setup(client):
    client.add_cog(Utils(client))