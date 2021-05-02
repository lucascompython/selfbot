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

with open(r"/home/lucas/Desktop/selfbot/token.txt", "r") as f:
    token = f.readlines()[0]

intents = discord.Intents.all()
bot = commands.Bot(description="Testeeeeeeee", command_prefix="+", self_bot=True, case_insensitive=True, intents=intents)





#token = "NzQ2MDg3NzgwNjQ3NDM2NDA5.YBk1mw.qvrZ8OWgZSE1S7ymZVg2L5mBTzQ"










@bot.event
async def on_ready():
    print(f'''{Fore.RED} _     _______________   ____  _____ _     _____ ____   ___ _____ 
| |   |___ /___ /_   _| / ___|| ____| |   |  ___| __ ) / _ \_   _|
| |     |_ \ |_ \ | |   \___ \|  _| | |   | |_  |  _ \| | | || |  
| |___ ___) |__) || |    ___) | |___| |___|  _| | |_) | |_| || |  
|_____|____/____/ |_|   |____/|_____|_____|_|   |____/ \___/ |_|  
                                                                  '''+Fore.RESET)
    print(f"{Fore.BLUE}O SelfBot está online"+ Fore.RESET)
    print("Esta logado como: {0.user}, id: {0.user.id}".format(bot))
    
    
    
    
    await bot.get_channel(818238584422662174).send("Selfbot is online!", tts=True)
    #await bot.get_channel(746087780647436409).send("bot is online")

    print(f"{Fore.MAGENTA}Desenvolvido por:{Fore.RESET} Lucas Maciel de Linhares\n{Fore.CYAN}Email:{Fore.RESET} lucasdelinhares@gmail.com\n{Fore.GREEN}Discord:{Fore.RESET} Lucas cheio da drip#3273")
    change_status.start()
    print("\n-----------------------------------------------------")
    print(f'{Fore.GREEN}Conectado em: {len(bot.guilds)} servers:' + Fore.RESET)
    for guild in bot.guilds:
        guild
        print(guild.name)
    

    print("-----------------------------------------------------")
    print(f'{Fore.CYAN}Link invite do otherbot: {Fore.MAGENTA}https://discord.com/api/oauth2/authorize?client_id=805878114415673385&permissions=8&scope=bot' + Fore.RESET)
    print(f'{Fore.CYAN}Link do Fiverr: {Fore.MAGENTA}https://www.fiverr.com/share/4bBZPR' + Fore.RESET)
    print("-----------------------------------------------------")
    pypy = 0
    for filename in os.listdir(r"/home/lucas/Desktop/selfbot/cogs/"):
        if filename.endswith(".py"):
            pypy += 1
            #print(filename)
    print(f"{Fore.YELLOW}Total Cogs: {str(pypy)}" + Fore.RESET)
    #server = bot.get_server(806176356671946814)
    #return server




for filename in os.listdir(r"/home/lucas/Desktop/selfbot/cogs/"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")






@bot.command()
async def ascii(ctx, *, args):
    await ctx.message.delete()
    text = pyfiglet.figlet_format(args)
    await ctx.send(f"```{text}```")



@bot.command()
async def negro(ctx, *, mensa):
    await ctx.message.delete()
    await ctx.send(f"**{mensa}**")



@bot.command()
async def tableflip(ctx):
    await ctx.message.delete()
    await ctx.send(f"(╯°□°）╯︵ ┻━┻")




@bot.command()
async def lenny(ctx):
    await ctx.message.delete()
    await ctx.send(f"( ͡° ͜ʖ ͡°)")


@bot.command()
async def teste(ctx):
    await ctx.message.delete()
    pimba = input("digite alguma cena: ")
    await ctx.send(pimba)




@bot.command()
async def ping(ctx):
    #await ctx.message.delete()
    #if ctx.author.id == 325986670824652800:
    print(f'O meu ping é: {round(bot.latency*1000, 3)} ms.')
    await ctx.send(f'O meu ping é: {round(bot.latency*1000, 3)} ms.')


@bot.command()
async def userinfo(ctx, *, user: discord.Member = None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author      
    date_format = "%a, %d %b %Y %I:%M %p"
    embed = discord.Embed(color=0xdfa3ff, description=user.mention)
    embed.set_author(name=str(user), icon_url=user.avatar_url)
    embed.set_thumbnail(url=user.avatar_url)
    try:
        embed.add_field(name="Juntou-se", value=user.joined_at.strftime(date_format))
    except:
        pass
    #members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
    #embed.add_field(name="Posiçao de entrada", value=str(members.index(user)+1))
    embed.add_field(name="Registrou-se", value=user.created_at.strftime(date_format))
    embed.add_field(name="Bot?", value=user.bot)
    embed.add_field(name="Status", value=f"{str(user.status).title()} \n {user.activity.name if user.activity else ''}")

    try:
        lçlç = "A ouvir no Spotify: "
        opop = lçlç + user.activities[1].title + "\nArtista: " + user.activities[1].artist + "\nAlbum: " + user.activities[1].album
        embed.add_field(name="Atividade", value=opop if user.activities[1] else '')
    except:
        embed.add_field(name="Atividade", value="N/A")
    embed.add_field(name="Boosted", value=bool(user.premium_since))
    num = random.choice([1, 2])
    if num == 1 or ctx.author.id == 325986670824652800:
        dripado = "True"
    else:
        dripado = "False"
    embed.add_field(name="Drip?", value=dripado)
    '''
    if len(user.roles) > 1:
        role_string = ' '.join([r.mention for r in user.roles][1:])
        embed.add_field(name="Cargos [{}]".format(len(user.roles)-1), value=role_string, inline=False)
    perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
    embed.add_field(name="Permissões no server", value=perm_string, inline=False)
    '''
    embed.set_footer(text='ID: ' + str(user.id))
    return await ctx.send(embed=embed)

@tasks.loop(seconds=2)
async def change_status():
    #await bot.change_presence(activity=discord.Game("em manutenção/pouco funcional"))´
    pass
'''
    nums = random.randrange(1, int(6))

    if nums == 1:
        await bot.change_presence(activity=discord.Game("com a tua mãe"))
    elif nums == 2:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="os gemidos da tua mãe"))
    elif nums == 3:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="os nudes da tua mãe"))
    elif nums == 4:
        await bot.change_presence(activity=discord.Streaming(name="a tua mãe", url="https://www.twitch.tv/litoosbds"))
    elif nums == 6:
        await bot.change_presence(activity=discord.Game("https://www.fiverr.com/share/4bBZPR"))
'''





@bot.command(aliases=["calc","cal"])
async def calculadora(ctx, num1):
    await ctx.message.delete()
    await ctx.send("Resposta: " + str(eval(num1)))



@bot.command(aliases=["sqrt","quadrada"])
async def raiz(ctx, num1 : float):
    await ctx.message.delete()
    await ctx.send(math.sqrt(num1))
    


@bot.command(aliases=["poder","pow"])
async def expoente(ctx, num1 : float, num2 : float):
    await ctx.message.delete()
    await ctx.send(pow(num1, num2))







@bot.command(name='1337-speak', aliases=['1337speak'])
async def _1337_speak(ctx, *, text): # b'\xfc'
    await ctx.message.delete()
    text = text.replace('a', '4').replace('A', '4').replace('e', '3')\
            .replace('E', '3').replace('i', '!').replace('I', '!')\
            .replace('o', '0').replace('O', '0').replace('u', '|_|').replace('U', '|_|')
    await ctx.send(f'`{text}`')

@bot.command()
async def everyone(ctx): # b'\xfc'
    await ctx.message.delete()
    await ctx.send('https://@everyone@google.com')



@bot.command()
async def empty(ctx): # b'\xfc'
    await ctx.message.delete()
    await ctx.send(chr(173))



@bot.command(name='drenado')
async def drenado(ctx, *, text): # b'\xfc'
    await ctx.message.delete()

    await ctx.send(f'***~~`{text}`~~***')




@bot.command()
async def secret(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    await ctx.send('||'+message+'||')


@bot.command()
async def reverse(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    message = message[::-1]
    
    await ctx.send(message)




@bot.command(help="Isto eh um comnado para ver o meu fiverr, DEIM ME O VOSSO DINHEIRO!")
async def fiverr(ctx):
    await ctx.message.delete()
    #user.id = 325986670824652800
    embed = discord.Embed(color=0xdfa3ff, description="Eu(<@325986670824652800>) sou pobre e custumo ir roubar arroz ao <@391325388216860676>, se quiseres podes me ajudar financieiramente :wink:.")
    embed.set_author(name="Lucas cheio da drip#3273", icon_url="https://cdn.discordapp.com/attachments/626449728988774401/819151902574116864/WhatsApp_Image_2021-01-04_at_11.20.52.jpeg")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/626449728988774401/819151902574116864/WhatsApp_Image_2021-01-04_at_11.20.52.jpeg")
    embed.add_field(name="Meu Fiverr", value="https://www.fiverr.com/share/4bBZPR")
    embed.set_footer(text="Pfv DEIM ME O VOSSO DINHEIRO!")
    await ctx.send(embed=embed)





@bot.command(name = 'serverinfo', help ="Este comando mostra a informação do server.")
async def serverinfo(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)





    statuses = [len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members)))]



    #roleCount = str(ctx.guild.role_count)
    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)
    #roleCount = str(ctx.guild.role_count)
    icon = str(ctx.guild.icon_url)
    
    embed = discord.Embed(
        title="Informação do Server: " + name ,
        #description=description,
        color=discord.Color.blue()
        )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Dono", value=owner, inline=True)
    embed.add_field(name="ID do Server", value=id, inline=True)
    embed.add_field(name="Região", value=region, inline=True)
    embed.add_field(name="Numero de Membros", value=memberCount, inline=True)
    embed.add_field(name="Humanos", value=len(list(filter(lambda m: not m.bot, ctx.guild.members))))
    embed.add_field(name="Bots", value=len(list(filter(lambda m: m.bot, ctx.guild.members))))
    embed.add_field(name="Utilizadores Banidos", value=len(await ctx.guild.bans()))
    
    embed.add_field(name="Canais de Texto", value=len(ctx.guild.text_channels))
    embed.add_field(name="Canais de Voz", value=len(ctx.guild.voice_channels))
    embed.add_field(name="Categorias", value=len(ctx.guild.categories))
    embed.add_field(name="Numero de Cargos", value=len(ctx.guild.roles))
    embed.add_field(name="Convites", value=len(await ctx.guild.invites()))
    embed.add_field(name="Status", value=f"🟢 {statuses[0]} 🟠 {statuses[1]} 🔴 {statuses[2]} ⚪ {statuses[3]}")
    
    #embed.add_field(name="Numero de Cargos", value=roleCount, inline=True)
    #embed.add_field(name='Numero de Bots:', value=(', '.join(list_of_bots)))

    await ctx.send(embed=embed)













@bot.command(name='gmail-bomb', aliases=['gmail-bomber', 'gmailbomb', 'email-bomber', 'emailbomber'])
async def _gmail_bomb(ctx): # b'\xfc'
    await ctx.message.delete()
    GmailBomber()




@bot.command(aliases=['slots', 'bet'])
async def slot(ctx): # b'\xfc'
    await ctx.message.delete()
    emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
    a = random.choice(emojis)
    b = random.choice(emojis)
    c = random.choice(emojis)
    slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"
    if (a == b == c):
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} All matchings, you won!"}))
    elif (a == b) or (a == c) or (b == c):
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} 2 in a row, you won!"}))
    else:
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} No match, you lost"}))






@bot.command(name = "spam", help ="Este comando serve para spamar alguem no privado com o bot.")
async def spam(ctx,memberr : discord.Member,  msgg,numberr = 10):
    #await ctx.send(memberr)
    await ctx.message.delete()
    queres = input("queres usar duplo spam? [s/n]")
    if queres == "s":
        quere = input("queres utilizar outra mensagem? [s/n]")
        if quere == "s":
            mensa = input("DIGITE UMA MENSAGEM: ")
            await ctx.send(f".spam <@{memberr.id}> {mensa} {numberr}")
        else:
            await ctx.send(f".spam <@{memberr.id}> {msgg} {numberr}")
        await ctx.send("SENTE O PODER DO DUPLO SPAM MUAAHAHAHA!")
    else:
        print("OKOKOK")
    #with open("spamnomes.txt", "w") as f:
        #f.write(cte.author)
    
    channell = await memberr.create_dm()
    #await ctx.send("Alvo spamado com sucesso.")
        #user = client.message.server.get_member(userid)
        #await member.kick(reason=motivo
        #await member.send_message(member,msg)
    for k in range(0,numberr):
        if msgg == "stop":
            break
            return
            #await ctx.send("pimba")
        await channell.send(msgg)
        time.sleep(1)

        #with open(r"C:\Users\lucas\Desktop\BOTDODISCORD\nome.txt", "w") as f:
            #f.write(member.id)

@bot.command(name='first-message', aliases=['firstmsg', 'fm', 'firstmessage'])
async def _first_message(ctx, channel: discord.TextChannel = None): # b'\xfc'
    await ctx.message.delete()  
    if channel is None:
        channel = ctx.channel
    first_message = (await channel.history(limit=1, oldest_first=True).flatten())[0]
    embed = discord.Embed(description=first_message.content)
    embed.add_field(name="Primeira mensagem", value=f"[Jump]({first_message.jump_url})")
    await ctx.send(embed=embed)





@bot.command(aliases=['guildpfp'])
async def guildicon(ctx): # b'\xfc'
    await ctx.message.delete()
    em = discord.Embed(title=ctx.guild.name)
    em.set_image(url=ctx.guild.icon_url)
    await ctx.send(embed=em)


@bot.command(name = "clear", help = "Este comando serve para dar clear a mensagens.")
async def clear(ctx, valor=5):
    await ctx.message.delete()
    await ctx.channel.purge(limit=valor)




@bot.command()
async def voice(ctx, sala: t.Optional[int], nume: t.Optional[int]):
    await ctx.message.delete()
    if nume == None:
        nume = 5
    if sala == None:
        channel = ctx.author.voice.channel
    else:
        channel = bot.get_channel(sala)
    for i in range(0, nume):
        await channel.connect()
        time.sleep(0.5)
        await ctx.voice_client.disconnect()

@bot.command(aliases=['será','serà'], help = "Este comando server para fazer uma pregunta ao bot.")
async def sera(ctx, *, pregunta):
    #respostas = ['De certeza que sim.','Provavelmente sim','Provavelmente não', 'De certeza que não', 'Sem duvida', 'Quase de certeza', 'Sim', 'Não','Não contes nisso','Duvido','o gui é gay']

    resposta = input("SERA: ")
    #await ctx.send("testeeee")
    await ctx.send(f'Pergunta: será {pregunta}\nResposta: {resposta}')





def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)



@bot.command(aliases=["rr", "reniciar", "restart"])
async def reboot(ctx):
    if ctx.author.id == 325986670824652800 or ctx.author.id == 746087780647436409:
        await ctx.send("A reniciar!")
        restart_program()
    else:
        await ctx.send("Não tens premissao para fazer isso! So o <@325986670824652800> é que pode.")

@bot.command(aliases=["privado"],name = "dm", help = "Este comando serve para enviar uma mensagem privada a alguem com o bot.")
async def dm(ctx,member : discord.Member, *,msg):
    await ctx.channel.purge(limit=1)
    global channel
    membro = member
    global escritor
    escritor = ctx.author
    #with open(r"C:\Users\lucas\Desktop\BOTDODISCORD\dmnomes.txt", "w") as f:
        #f.write(escritor)
    channel = await member.create_dm()
    

    await channel.send(msg) 
    #with open(r"C:\Users\lucas\Desktop\BOTDODISCORD\nome.txt", "w") as f:
        #f.write(member.id)








#erros
@bot.event
async def on_command_error(ctx, error):

    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.message.delete()
        print('Por favor escreva todos os argumentos.')

    elif isinstance(error, commands.MemberNotFound):
        await ctx.message.delete()
        print('Membro não encontrado.')

    elif isinstance(error, commands.CommandNotFound):
        await ctx.message.delete()
        print('Comando não existe.\nPara mais informação sobre os comandos use "help".')
    
    elif isinstance(error, commands.BotMissingAnyRole):
        await ctx.message.delete()
        print('Não tenho permissões para tal coisa.')

    elif isinstance(error, commands.BotMissingPermissions):
        await ctx.message.delete()
        print('Não tenho permissões para tal coisa.')

    elif isinstance(error, commands.BotMissingRole):
        await ctx.message.delete()
        print('Não tenho permissões para tal coisa.')

    elif isinstance(error, commands.MissingPermissions):
        await ctx.message.delete()
        print('Não tem permissões para tal coisa.')

    elif isinstance(error, commands.BadArgument):
        await ctx.message.delete()
        print('Argumento invalido.')






@bot.command()
async def load(ctx, *,extension):
    if ctx.author.id == 325986670824652800 or ctx.author.id == 746087780647436409:
        try:
            bot.load_extension(f"cogs.{extension}")
            await ctx.send(f"{extension} foi carregada")
        except:
            await ctx.send("Cog não encontrada ou ta com problemas!")
    else:
        await ctx.send("So o <@325986670824652800> é que pode usar esse comando!")
@bot.command()
async def unload(ctx, *,extension):
    if ctx.author.id == 325986670824652800 or ctx.author.id == 746087780647436409:
        try:
            bot.unload_extension(f"cogs.{extension}")
            await ctx.send(f"{extension} foi descarregada")
        except:
            await ctx.send("Cog não encontrada ou ta com problemas!")
    else:
        await ctx.send("So o <@325986670824652800> é que pode usar esse comando!")
    


@bot.command()
async def reload(ctx, *,extension):
    if ctx.author.id == 325986670824652800 or ctx.author.id == 746087780647436409:
        try:
            bot.unload_extension(f"cogs.{extension}")
            bot.load_extension(f"cogs.{extension}")
            await ctx.send(f"{extension} foi recarregada")
        except:
            await ctx.send("Cog não encontrada ou ta com problemas!")
    else:
        await ctx.send("So o <@325986670824652800> é que pode usar esse comando!")







@bot.command()
async def encode(ctx, string): # b'\xfc'
    await ctx.message.delete()
    decoded_stuff = base64.b64encode('{}'.format(string).encode('ascii'))
    encoded_stuff = str(decoded_stuff)
    encoded_stuff = encoded_stuff[2:len(encoded_stuff)-1]
    await ctx.send(encoded_stuff) 

@bot.command()
async def decode(ctx, string): # b'\xfc'+
    await ctx.message.delete()  
    strOne = (string).encode("ascii")
    pad = len(strOne)%4
    strOne += b"="*pad
    encoded_stuff = codecs.decode(strOne.strip(),'base64')
    decoded_stuff = str(encoded_stuff)
    decoded_stuff = decoded_stuff[2:len(decoded_stuff)-1]
    await ctx.send(decoded_stuff)






@bot.command(aliases=['ri', 'role'])
async def roleinfo(ctx, *, role: discord.Role): # b'\xfc'
    await ctx.message.delete()
    guild = ctx.guild
    since_created = (ctx.message.created_at - role.created_at).days
    role_created = role.created_at.strftime("%d %b %Y %H:%M")
    created_on = "{} ({} days ago)".format(role_created, since_created)
    users = len([x for x in guild.members if role in x.roles])
    if str(role.colour) == "#000000":
        colour = "default"
        color = ("#%06x" % random.randint(0, 0xFFFFFF))
        color = int(colour[1:], 16)
    else:
        colour = str(role.colour).upper()
        color = role.colour
    em = discord.Embed(colour=color)
    em.set_author(name=f"Nome: {role.name}"
    f"\nRole ID: {role.id}")
    em.add_field(name="Utilizadores", value=users)
    em.add_field(name="Mentionavel", value=role.mentionable)
    em.add_field(name="Hoist", value=role.hoist)
    em.add_field(name="Posiçao", value=role.position)
    em.add_field(name="Managed", value=role.managed)
    em.add_field(name="Cor", value=colour)
    em.add_field(name='Dia da criaçao', value=created_on)
    await ctx.send(embed=em)




@bot.command()
async def masscon(ctx, _type, amount: int, *, name=None): # b'\xfc'
    await ctx.message.delete()
    payload = {
        'name': name,
        'visibility': 1 
    }
    headers = {
        'Authorization': token,
        'Content-Type':'application/json', 
    }
    avaliable = [
        'battlenet',
        'skype',
        'leagueoflegends'
    ]
    if name is None:
        name = 'about:blank'
    elif _type not in avaliable:
        print(f'Avaliable connections: {avaliable}')
    for _i in range(amount):
        try:
            ID = random.randint(10000000, 90000000)
            time.sleep(5) 
            r = requests.put(f'https://canary.discordapp.com/api/v6/users/@me/connections/{_type}/{ID}', data=json.dumps(payload), headers=headers)
            if r.status_code == 200:
                print(f"[{Fore.GREEN}+{Fore.RESET}] New connection added!")
            else:
                print(f"[{Fore.RED}-{Fore.RESET}] Couldnt add connection!");break
        except (Exception, ValueError) as e:
            print(e);break
    print(f"[{Fore.GREEN}+{Fore.RESET}] Finished adding connections!")





    
#bot.loop.create_task(runtime_background_task())
bot.run(token, bot=False, reconnect=True)
############################### refazer o fiver ######################## 
################################# fazer mais um anuncio no fiver #########
################################## comentar as drenas antes dos imports ##############################
'''
I will make a CUSTOM bot of your choice and help you set it up, interact with it, and how to host it!



The things I can provide for your bot:

BASIC BOT:

Specific owner commands(Reload, load, unload, serverinfo)
Moderation(kick, ban, unban, ping, clear, mute, unmute, and more!)
Fun(8ball, Reddit commands, random meter, today, ppsize, and more!)
Economy(gifting, profiles, gambling)
STANDARD BOT:

all the features from the basic bot
Social(Marry, divorce, hug, kiss, hit, and more!)
Specific owner commands (announce, avatar, snipe message, command toggle, //user logs//, and more!)
Music(play, pause, repeat, resume, queue, now playing, disconnect, and more!)
Economy(shops, custom events, bank, investing, daily, achievements)
PREMIUM BOT:

all the features from the standard bot and basic bot
Waifu generator (feed, rename, view, talk, pet, gift, inventory, marketplace, generates a never-before-seen waifu)
general(Wikipedia search, google translate, poll, and more!)
Social(NSFW commands)
RPG game in discord system
Economy(Leaderboards, voting(top.gg only), profile customization, level and xp system)


for anything else, DM me first.
'''