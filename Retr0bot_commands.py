import discord
from discord.ext import commands, tasks
import random

client = discord.Client()



players = {}

dscArray = ['PEDO ALERT! PEDO ALERT!', 'ALERT! FIND LOCAL PEDOS WITH THIS TOOL!', 'WARNING PEDO FOUND IN YOUR AREA!', 'OH NO PEDOMAN786 HAS SIGHT OF A CHILD!', 'LEFT FUCKING BUGGER']

messageArray = ['This is a public service announcement:', 'Hi, im here to inform you that we know YOU are a pedo (uwais...)',]


imgArray = ['https://cdn.discordapp.com/attachments/450308031906054146/779095559709523989/unknown.png',
            'https://cdn.discordapp.com/attachments/450308031906054146/779808431288352768/ezgif.com-gif-maker.gif',
            'https://cdn.discordapp.com/attachments/778646771584335906/779808940787499018/photo.PNG',
            'https://cdn.discordapp.com/attachments/778646771584335906/779808936877621318/unknown.png',
            'https://cdn.discordapp.com/attachments/778646771584335906/779808933245091840/EVeSJdnXgAAqfAQ.jpg',
            'https://cdn.discordapp.com/attachments/778646771584335906/779808931673145344/v7H7C9ZN_400x400.jpg',
            'https://cdn.discordapp.com/attachments/778646771584335906/779808929839841280/c0827a70a97dce15248c972b137c1cdf--beefy-men-hairy-men.jpg',
            'https://cdn.discordapp.com/attachments/778646771584335906/779808927378309130/bBdVT1n1_400x400.jpg',
            'https://cdn.discordapp.com/attachments/778646771584335906/809793712401023066/clowns-dreams-nakedoldman.png',
            'https://cdn.discordapp.com/attachments/778646771584335906/809790253068976158/Portfolio_Clownville_The_Butcher.png',
            'https://cdn.discordapp.com/attachments/778646771584335906/809789947132903516/unknown.png',
            'https://cdn.discordapp.com/attachments/778646771584335906/809503188918992956/image0.png',
            'https://cdn.discordapp.com/attachments/778646771584335906/809106930646777878/MWA_greatest_hits.png']


def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


bot = commands.Bot(command_prefix='!')

token = read_token() 


@bot.command()
async def status(ctx , activity, *, args):
    activity = activity.lower()
    if activity == "playing":
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=args))

    if activity == "listening":
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=args))

    if activity == "watching":
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=args))


@bot.command()


async def moveuser(ctx, member:discord.Member, args):
    if ctx.message.author.id != 267045440631865344:
        return

    channel = 0

    if args == "General":
        channel = 778646771584335907
        await ctx.send("User Moved!")

    if args == "Rust":
        channel = 779422096040001536
        await ctx.send("User Moved!") 

    if args == "Cod":
        channel = 779422163945127956
        await ctx.send("User Moved!")

    if args == "RL":
        channel = 779422212343988264
        await ctx.send("User Moved!")

    if args == "Music":
        channel = 788842749829840926
        await ctx.send("User Moved!")

    if args == "Movies":
        channel = 801247362739339265
        await ctx.send("User Moved!")

    if args == "Remove":
        channel = None
        await ctx.send("User Removed!")


    await member.edit(voice_channel=ctx.guild.get_channel(channel))


@bot.command(pass_context=True)
async def rename(ctx, member: discord.Member, nick):
    if ctx.message.author.id != 267045440631865344:
            embed = discord.Embed(
                title = "You Cant Rename!",
                description = "nice try",
                colour = discord.Colour.red()
            )
            randomImage = 'https://cdn.discordapp.com/attachments/450308031906054146/779808431288352768/ezgif.com-gif-maker.gif'
            embed.set_image(url=randomImage)
            await ctx.send(embed=embed) 
            return
    await member.edit(nick=nick)




bot.run(token)
    
