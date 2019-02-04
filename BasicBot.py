import discord, random, asyncio, requests, wod
from discord.ext.commands import Bot, has_permissions
from xml_bs4 import get_xml_data, build_url, get_img_urls, parse_urls, parse_xml
"""
ADD:
- Change game status
- Make a special command for p stars

Hard, but important:
- Fix inputing command args
"""
cmd_prefixs = ("$","!")
bot = Bot(command_prefix=cmd_prefixs, description='Does everything from bascic functions to full-on porn')
bot.remove_command('help')

token = 'NDEzNjc2NTQ1NTU5ODg3ODcy.DW2g2Q.opfBZrh3JNmCry3XVDIUCR8A0Y0'

"---------------Events-----------------"
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_member_join(member):
	dumb_phrases = ['Skeet fast, eat ass - Jasper S', "Watashi wa Skeetaa Davis desu", "Where is your fucking CAS work - IB staff"]
	random.shuffle(dumb_phrases)
	role_to_add = discord.utils.get(member.guild.roles, name="Guinea Pig")
	await member.add_roles(role_to_add)
	for channel in member.guild.channels:
		if channel.name == 'general':
			await channel.send("Welcome {member.name}"+ str(random.choice(dumb_phrases)))
@bot.event
async def on_message(message):   
	if message.author == bot.user:
		return 	
	print("user has sent a msg") 
	await bot.process_commands(message) # Keep this line below the if statments, or it will conflict with the commands


"---------------Commands----------------"
@bot.command()
async def help(ctx):
	embed = discord.Embed(title="MrSmithChan", description="A Very Nice bot. List of commands are:", color=0xeee657)
	embed.add_field(name="$help", value="Gives this message", inline=False)
	embed.add_field(name="$greet", value="Gives a message to the user", inline=False)
	embed.add_field(name="$ping", value="Gives a message with whatever the user types", inline=False)
	embed.add_field(name="$r34", value="Gives images of a tag (or tags) based on a certain number. Example: $r34 Furry 3", inline=False)
	embed.add_field(name="$wod", value="Give a message with the word of the day",inline=False)
	#embed.add_field(name=, value=,inline=False)
	await ctx.send(embed=embed)

@bot.command()
async def mute(ctx,member: discord.Member):
	await member.server_voice_state(member,mute=True)
	await ctx.send('{} has been muted.'.format(member.mention))

@bot.command(aliases=["r34","34"])
async def rule34API(ctx,tag,limit:int = 1):
	tag = tag.lower()
	if limit > 13:
		new_limit = random.randint(0,13)
		#await ctx.send("Slow your roll my nizzle, you just tried to enter " + str(limit) + " I will display" + str(new_limit) + "images, and get that CAS shit done, Tyrone, sorry I meant" + ctx.author)
		await ctx.send("Slow your roll my nizzle, you just tried to enter {} images I will show instead {} images, and get that CAS shit done, Tyrone, sorry I meant {}. ".format(limit,new_limit,ctx.author.name))
		limit = new_limit
	urls =  parse_urls(limit,urls=get_img_urls(parse_xml(get_xml_data(build_url(tag)))))
	for url in urls:
			await ctx.send(url)

@bot.command()
async def ping(ctx,*args):
	await ctx.send(args)	
@bot.command()
async def greet(ctx):
	await ctx.send("Why hello there {}!".format(ctx.message.author.name))
	
@has_permissions(administrator=True)
@bot.command()
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)

@bot.command(aliases=["wod"])
async def WOD(ctx):
	Soup = wod.soup
	date = wod.getTodayDate(Soup)
	word = wod.GetWordOfThedayHtml(Soup)
	definintions = wod.GetWordDefinition(Soup)
	word_attribs = wod.GetWordAtttributes(Soup)
	embed = discord.Embed()
	embed.add_field(name="Date",value=date, inline=False)
	embed.add_field(name="Word", value=word, inline=False)
	embed.add_field(name="Word Attributes", value=', '.join("{}: {}".format(key,val) for (key,val) in word_attribs.items()), inline=False)
	embed.add_field(name="Definitions", value=", ".join("{}".format(definintion) for definintion in definintions), inline=False)
	await ctx.send(embed=embed)

@has_permissions(administrator=True)
@bot.command()
async def add_user_role(ctx, *,role):
	user = ctx.author
	role_to_add = discord.utils.get(ctx.guild.roles, name=role)
	await user.add_roles(role_to_add)
	
"-----------------Errors-----------------"
@rule34API.error
async def rule34API_on_error(ctx,error):
	embed = discord.Embed()
	embed.add_field(name="Error: tag fuck up", value="Check spelling or tag doesn't exist\n Also, make sure u put a number for the limit \n TIP: Use an underscore if one tag has more than one word, and a plus sign for multiple tags", inline=False)
	await ctx.send(embed=embed)

"-----------------Tests-------------------"
bot.run(token)

# The help command is currently set to be not be Direct Messaged.
# If you would like to change that, change "pm_help = False" to "pm_help = True" on line 9.