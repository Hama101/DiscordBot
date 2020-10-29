import requests
from bs4 import BeautifulSoup
import pandas as pd
import discord
from discord.ext import commands
import youtube_dl
import R6stat
import CovidTracker
import Movie_bloger
import Tv_Show
import GameFinder
import R6bio

client = commands.Bot(command_prefix=".")


# stat commande
@client.command(aliases=["Stats", "stat", "st"])
async def Stat(ctx, *, playerName):
    await ctx.send("hello Stat : " + playerName)
    # print(findStat(playerName))
    s = R6stat.findStat(playerName)
    for i in s:
        await ctx.send(i + "\n")
        print(i + "\n")


# covid-19 tracker
@client.command(aliases=["Corona", "Covid-19", "Covid"])
async def covid(ctx, *, contry):
    try:
        await ctx.send("Hello to Discord Bot Covid-19 tracker for "+contry+"!")
        await ctx.send(CovidTracker.covidStat(contry))
    except:
        await ctx.send('```diff\n -**Error Please check contrey name again!** \n```')

#OpBoi finder 
@client.command(aliases=["Bio","R6op","bio"])
async def R6opBio (ctx , * , opName):
    try:
        await ctx.send("R6 Ops")
        await ctx.send(R6bio.findBio(opName))
    except:
        await ctx.send('```diff\n -**Error Please check Op name again!** \n```')

# Movie info command
@client.command(aliases=["M", "Movie", "Mv", "mv"])
async def movie(ctx, *, movieName):
    try:
        await ctx.send("Hello to Discord Bot Movie for the night is " + movieName + "!\n")
        await ctx.send(Movie_bloger.movieInfos(movieName))
    except:
        await ctx.send('```diff\n -**Error Please check Movie name again!** \n```')


# tv show command
@client.command(aliases=["Sh", "Show", "sh"])
async def show(ctx, *, showName):
    try:
        await ctx.send("Hello to Discord Bot Show for the night is " + showName + "!\n")
        await ctx.send(Tv_Show.tvShow(showName))
    except:
        await ctx.send('```diff\n -**Error Please check Show name again!** \n```')

# Game Finder Command
@client.command(aliases=["Game", "gm", "Gm"])
async def game(ctx, *, gameName):
    try:
        await ctx.send('Hello to Discord Game finder Bot !')
        await ctx.send(GameFinder.gameFinder(gameName))
    except:
        await ctx.send('```diff\n -**Error Please check Game name again!** \n```')




# Ready ?
@client.event
async def on_ready():
    print('I m ready !')

# ping commmande
@client.command()
async def ping(ctx):
    await ctx.send(f'Ping  : {round(client.latency * 1000)} ms')

# ShutDown Command
@client.command(aliases=['sd', 'SD'])
async def shutdown(ctx):
    print("shutdown")
    await ctx.send("Reached target [Shutdown]")
    await client.logout()
    client.clear()


@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()


@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()


@client.event
async def on_member_join(member, ctx):
    print(f'{member} has joined the server !')
    await ctx.send(f'{member} has joined the server !')


@client.event
async def on_member_remove(member, ctx):
    print(f'{member} has left the server !')
    await ctx.send(f'{member} has left the server !')

client.run('NzU4NjQ4NDUyNTg5ODEzNzYw.X2yAbg.D-UMHTM5eS0zlwOwUBW8ciUrd1Y')
