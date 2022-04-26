############################ dependicies ################################
from datetime import date, datetime
from math import floor
from random import choice
import discord
from discord import FFmpegPCMAudio
from discord.ext import commands
from cenzo import cenzo
from os.path import exists
import text
import funkcja
import youtube_dl
import os

############################ GLOBALE ################################
TOKEN = "censoredcensoredcensoredcensoredcensoredcensoredcensored"
DESCRIPTION = "ADam" #MY BOT
GRYGIER_USER_ID = "297792622871838720"


intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='-', description=DESCRIPTION, intents=intents)# Bot check for "-" text prefix on chat

############################ RAPORT ################################
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle)
    print(text.start[0], client.user.name, client.user.id, text.start[1])

############################ KOMENDY DOLACZENIA I WYJSCIA ################################
@client.event
async def on_member_join(member):
    channel = client.get_channel(946024615522734110) #mess. channel
    channel.send("Witamy...")


@client.event
async def on_member_remove(member):
    channel = client.get_channel(946024615522734110)
    channel.send("Zegnam")


@client.command(ban_members = True)
async def kick(ctx, member: discord.Member, *, reason="censored"):
    await member.kick(reason=reason)
    await ctx.send(f'Banned')

############################ KOMENDY MUZYCZNE ################################

@client.command(pass_context=True)#Podłączenie bot-a
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send("Połączono.")
    else:
        await ctx.send("Vc jest pusty...")


@client.command(pass_context=True)# bot pobiera film z YT w formacie MP3 i puszcza go na kanale
async def yt(ctx, url):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        voice = await channel.connect()
        file_exists = exists("song.mp3")
        if file_exists:
            os.remove("song.mp3")
        ydl_opts = {
            "format": "bestaudio/best",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",#jakosc
            }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, "song.mp3")

        source = FFmpegPCMAudio("song.mp3")
        player = voice.play(source)
        await ctx.channel.purge(limit=1)
        await ctx.send(f"Gram z yt {url}")
    else:
        await ctx.send("Vc jest pusty...")


@client.command(pass_context=True)
async def wyjazd(ctx):
    if ctx.voice_client:
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Bye")
    else:
        await ctx.send("Nie ma mnie na vc...")


@client.command(pass_context=True)#Pause...
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        await ctx.send("Paused...")
        voice.pause()
    else:
        await ctx.send("Brak MP3 które mogę zatrzymać...")


@client.command(pass_context=True)#resume...
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        await ctx.send("Wznawiam...")
        voice.resume()
    else:
        await ctx.send("Brak MP3 które mogę wznowić...")


@client.command(pass_context=True)
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()


@client.command(pass_context=True)
async def zagraj_z_dysku(ctx):
    try:
        voice = ctx.guild.voice_client
        randomy = choice(cenzo)
        source = FFmpegPCMAudio(randomy)
        try:
            voice.play(source)
            await ctx.send(f"Gram: [{randomy[6:36]}]")#Skrócona nazwa
        except AttributeError:
            channel = ctx.author.voice.channel
            await ctx.send("```Problem z kanałem.\nJuż wykonuję korekte.```")
            await channel.connect()
            voice = ctx.guild.voice_client
            voice.play(source)
            await ctx.send(f"Gram: [{randomy[6:36]}]")
    except discord.errors.ClientException:
        await ctx.send("```Już gram mp3, czekaj lub wydaj poleceie '-stop'```")


############################ KOMENDY CZATU ################################

@client.command()
async def adas(ctx):
    await ctx.send("censored")


@client.command()
async def siema(ctx):
    await ctx.send("Hello")


@client.command()# we play every sunday
async def sunday(ctx):
    now = datetime.now()
    dzien = now.day
    if dzien == 6:
        await ctx.send(text.dzien[0])
    else:
        await ctx.send(text.dzien[1])


############################ KOMENDY DATY ################################
@client.command()#My BD date
async def papiezdata(ctx):
    now = datetime.now()
    delta = date(now.year, now.month, now.day) - date(2001, 2, 28)
    lata = floor(delta.days / 365)
    await ctx.send(f"```diff\nOd 28.02.2001 mineło {lata} lat i {delta.days - (lata * 365)} dni...\n```")


@client.command()
async def ile(ctx):
    now = datetime.now()
    delta = date(2001, 5, 2) - date(now.year, now.month, now.day)
    ile_dni = (delta.days - (floor(delta.days / 365) * 365)) - floor(delta.days / 365)
    await ctx.send(f"Jeszcze {ile_dni} dni do urodzin...")


@client.command() #sends hours to my online chart, then post link so u can check how many hours do u play
async def ligaczas(ctx, arg1):
    funkcja.tabela(arg1)
    if float(arg1) > 4:
        await ctx.send(f"Holy molly {arg1} hours?!\nU will loose ur mind")
    await ctx.send("check this out https://pixe.la/v1/users/aapa123daaw/graphs/graph1.html")


############################ KOMENDY TELEFON ################################
@client.command()#Friends phone numbers
async def numerytel(ctx):
    await ctx.send(text.tel)
    now = datetime.now()
    print(f"Podano numery {now}")#console raport


@client.command()# bot sends message on my friends FB group
async def fb(ctx):
    funkcja.fb()
    await ctx.send("Wysłano")


@client.command()#Send SMS to numbers i set
async def sms(ctx):
    numery = ["+48 111 111 111", "+48 796 123 425"]
    await ctx.send("Wysłałem sms na numery:")
    funkcja.SMS(numery)
    for numer in numery:
        await ctx.send(f"{numer}")


############################ KOMENDY PLAN ################################
@client.command()# School schedule webpage link will be posted on DC app group
async def plan(ctx):
    await ctx.send(SCHOOL PLAN LINK)


@client.command()
async def mecz(ctx):
    text = funkcja.mecz()
    await ctx.send(text)


@client.command()
async def nextmecz(ctx):
    text = funkcja.nextmecz()
    await ctx.send(text)


############################ KOMENDY LOSUJ ################################
@client.command()
async def ligapozycje(ctx, arg1):
    pozycje = ["TOP", "MID", "JG", "ADC", "SUP"]
    lista_graczy = arg1.split(",")
    now = datetime.now()
    print(f"wybierano pozycje {now}")# raport
    if len(lista_graczy) <= 5:
        for person in lista_graczy:
            poz = choice(pozycje)
            pozycje.remove(poz)
            await ctx.send(f"{person} gra na pozycji {poz}")
    else:
        await ctx.send("Za dużo typa, wtf")#too much ppl (wtf==Why The Freak)


@client.command()
async def ktobot(ctx, arg1):
    lista_graczy = arg1.split(",")
    wybraniec = choice(lista_graczy)
    await ctx.send(f"{wybraniec} grasz bota")


############################ KOMENDY CZYSC KANAL ################################
@client.command()#Channel cleaner
async def czysckanal(ctx, ilosc: int):
    if ilosc == 0:
        await ctx.send("Brak zmiennej dot. ilości wiadomości jakie mam usunąć")
    elif ilosc >= 5000:
        await ctx.send("Hola, hola, to zbyt wiele...")
    else:
        await ctx.channel.purge(limit=ilosc)
        print(f"Wyczyszczono z {ilosc} elementów")


client.run(TOKEN)