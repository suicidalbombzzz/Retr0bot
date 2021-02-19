import discord
import random
from discord.ext import commands, tasks
from itertools import cycle
import asyncio




def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

status = cycle(['test1', 'test2'])

token = read_token()



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

messageArray = ['This is a public service announcement:', 'protecting your compooter from wirus with your credit card details since raj found this place on craigslist', 'Hi, im here to inform you that we know YOU are a pedo (uwais...)', 'Alert, daal located in microwave (oh bilal...)']
dscArray = ['PEDO ALERT! PEDO ALERT!', 'UH OH, SOMEBODY IS TRYING TO STEAL YOUR CREDIT CARD DETAILS! (vishwa.....)', 'ALERT! FIND LOCAL PEDOS WITH THIS TOOL!', '*goes to top of stairs*, *shouts* "PAKIS"', 'HELLO YOUR COMPOOTER HAVE WIRUS']
bot = commands.Bot(command_prefix='!')
#channel = client.get_channel(726151905180647575)




@bot.event



#On message will send a message only when teh people in the array say something
@bot.event


async def on_message(message):

    vicID = [745037897157312512, 207147098255130625, 280675613755572225, 779290910659706890, 434424519231406088, 779292300386893825]
    if message.author.id not in vicID :
        return
#help command
    if message.content.find("!help") != -1:
        await message.channel.send("shut the fuck up, all i do is insult a list of people every time they send a message.")

    if message.content.find("!insultme") != -1:
            insArray = ['You smell like curry', 'Shut the fuck up you stupid pedo', 'My pedo detection is off the charts! ALERT THERE IS A PEDO IN OUR MIDST!', 'PEDO PEDO PEDO PEDO']
            insMsg = insArray[random.randint(0,len(insArray)-1)]
            await message.channel.send(insMsg)

    

    randMsgArray = ['This is a public service announcement:', 'protecting your compooter from wirus with your credit card details since raj found this place on craigslist', 'Hi, im here to inform you that we know YOU are a pedo (uwais...)', 'Alert, daal located in microwave (oh bilal...)']

    randnum = random.randint(0,1000000)
    
    if randnum == 5000:
        randMsg = randMsgArray[random.randint(0,len(randMsgArray)-1)]
        await message.channel.send(randMsg)
    channel = bot.get_channel(message.channel.id)
    randomMessage = messageArray[random.randint(0,len(messageArray)-1)]
    descriptionMsg = dscArray[random.randint(0,len(dscArray)-1)]
    embed = discord.Embed(
                title = randomMessage,
                description = descriptionMsg,
                colour = discord.Colour.red()
            )
    bedArray = ['Vishwa is a hippie scammer!', 'uwais is a PEDO!', 'oi haroon, phantomforces is shit', 'Vishwa cant do kick flip "hehehehehehe"', 'uwais LOVES cock', 'bilal your music taste is shit']
    randomImage = imgArray[random.randint(0,len(imgArray)-1)]
    randomMsg = bedArray[random.randint(0,len(bedArray)-1)]
    embed.set_image(url=randomImage)
    embed.set_footer(text=randomMsg)
    await channel.send(embed=embed) 






#sends a message when a new person joins the server




bot.run(token)
