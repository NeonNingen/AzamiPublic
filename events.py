import discord, os, random
from discord.ext import commands, tasks
from discord.ext.commands import CommandNotFound

# Initializing Azami
azami = commands.Bot(command_prefix = 'a!',
					 description = "Azami, an all purpose bot!",
					 owner_id = 639574438794231818)

def event_azami():

	#Change this list if you add/remove cogs
	cogs = ['basic',
		'dnd',
		'fun', 
		'help',
		'jojo',
	        'maths',
	        'mod',
	        'owner',
	        'server',
	        'CommandErrorHandler'
	       ]
	
	for cog in cogs:
		azami.load_extension(f'cogs.{cog}')
		print(f'The following cog has been loaded: {cog}')

	@azami.event
	async def on_ready(): # Message when logged in on console
		await azami.change_presence(activity=discord.Activity(
			name=(
				f"a!help for help | {len(azami.guilds)} servers | Epic Version"), type=discord.ActivityType.playing))
		print(f"We have logged in as {azami.user}")	

		
	#If using a db perhaps consider storing welcome/goodbye channels then sending an embed to them on these next two events
	@azami.event
	async def on_member_join(member):
		print(f"{member} has joined {member.guild}")

	@azami.event
	async def on_member_remove(member):
		print(f"{member} has left/kick from {member.guild}")	

	@azami.event
	async def on_guild_join(guild: discord.Guild): # Join message on guild
		cogs = [c for c in azami.cogs.keys()]
		store = 0
		for cog in cogs:
			cogc = azami.get_cog(cog).get_commands()
			store += len(cogc)
		channel = guild.system_channel
		if channel.permissions_for(guild.me).send_messages:
			embed = discord.Embed(title="Hi there!",
								  description=f"{guild.name}, I'm so excited to be here!",
								  color=discord.Color.gold())
			embed.set_thumbnail(url=guild.icon_url)
			embed.set_footer(text=f"I'm in {len(azami.guilds)} guilds!")
			value1 = f"I'm an all purpose bot with currently:\n **{len(cogs)} cogs** and **{store} commands**"
			value2 = f"It's a pleasure to make your Acquaintance, {guild.owner.mention}"
			embed.add_field(name=f"Hi, my name is {azami.user.name}", value=value1)
			embed.add_field(name=f"To read about my commands, do {azami.command_prefix}help", value=value2)
			await channel.send(embed=embed)

def main(): # Actual main function xD
	event_azami()
	try:
		azami.run(os.environ['DISCORD_TOKEN'])
	except:
		token = open("token.txt", "r")
		azami.run(token.read())

