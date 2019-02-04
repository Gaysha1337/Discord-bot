import discord, asyncio, random, requests, rule34_test
from discord.ext import commands
from bs4 import BeautifulSoup

token = 'NDEzNjc2NTQ1NTU5ODg3ODcy.DW2g2Q.opfBZrh3JNmCry3XVDIUCR8A0Y0'
bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="MrSmithChan", description="Litest shit ever fam.", color=0xeee657)
    # give info about you here
    embed.add_field(name="Author", value="Gaysha")
    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")
    # give users a link to invite thsi bot to their server
    embed.add_field(name="Invite", value="[Invite link](<not yet, but soon>)")
    await ctx.send(embed=embed)

@bot.command()
async def greet():
    await bot.say(":smiley: :wave: Hello, there!")

@bot.command()
async def RULE34(ctx,tag):
    await ctx.say(tag)

@bot.event
async def on_message(message):
    word_list = ["Vegans be gone", "DAD^2!!!","Yall Gay","I am the thicc"]    
    if message.content.startswith('$ping'):
       await bot.send_message(message.channel, random.choice(word_list))
    elif message.content == "$DAD":
        await bot.send_message(message.channel, ":regional_indicator_n: :regional_indicator_u: :regional_indicator_t: :weary: :eggplant: :sweat_drops:")
    elif message.content == "$BAWDEN":
        await bot.send_message(message.channel, "https://img.rule34.xxx/images/2233/142844d6124bdbad367086556accadb0.jpeg")

bot.run(token)