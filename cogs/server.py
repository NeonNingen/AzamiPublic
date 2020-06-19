import discord, aiohttp, time
from discord.ext import commands
from random import choice

color_list = [discord.Color.red(), discord.Color.green(), discord.Color.blue()]

# In Azami 2.0: Use a import system for the colours like eg. from cogs.color import color_list
# ah old comments, quite amazing not gonna lie.

async def hastebin(content, session=None): # Move to cogs/utils/check in future
	session = aiohttp.ClientSession() # Yh that actually happens in the future!
	async with session.post("https://hastebin.com/documents", data=content.encode('utf-8')) as resp:
		if resp.status == 200:
			result = await resp.json()
			await session.close()
			return "https://hastebin.com/" + result["key"]
		else:
			return f"Error with creating Hastebin, Status: {resp.status}"
	
		

class Server(commands.Cog):

	def __init__(self, azami):
		self.azami = azami

	@commands.command(description='This will display info about the server', aliases=["si"])
	async def serverinfo(self, ctx):
		server = ctx.message.guild
		online = 0
		for i in server.members:
			if str(i.status) == 'online' or str(i.status) == 'idle' or str(i.status) == 'dnd':
				online += 1
		all_users = []
		for user in server.members:
			all_users.append(f'{user.name}')
		all_users.sort()
		_all = '\n'.join(all_users)
		channel_count = len([x for x in server.channels if type(x) == discord.channel.TextChannel])
		role_count = len(server.roles)
		emoji_count = len(server.emojis)
		em = discord.Embed(name="Server Info",
						   description= f"For the server: {server.name}",
						   color=choice(color_list))
		em.add_field(name='Name', value=server.name)
		em.add_field(name='Owner', value=server.owner, inline=False)
		em.add_field(name='Members', value=server.member_count)
		em.add_field(name='Currently Online', value=online)
		em.add_field(name='Text Channels', value=str(channel_count))
		em.add_field(name='Region', value=server.region)
		em.add_field(name='Verification Level', value=str(server.verification_level))
		em.add_field(name='Highest role', value=server.roles[role_count - 1])
		em.add_field(name='Number of roles', value=str(role_count))
		em.add_field(name='Number of emotes', value=str(emoji_count))
		url = await hastebin(str(_all), None)
		hastebin_of_users = f'[List of all {server.member_count} users in this server]({url})'
		em.add_field(name='Users', value=hastebin_of_users)
		em.add_field(name='Created At', value=server.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
		em.set_thumbnail(url=server.icon_url)
		em.set_author(name='Server Info', icon_url=self.azami.user.avatar_url)
		em.set_footer(text='Server ID: %s' % server.id)
		await ctx.send(embed=em)

		

	@commands.command(description='This will display info about user or another user', aliases=["ui"])
	async def userinfo(self, ctx, *, name=""):
		if name:
			user = user = ctx.message.mentions[0]
		else:
			user = ctx.message.author

		if isinstance(user, discord.Member):
			role = user.top_role.name
			if role == "@everyone":
				role = 'N/A'

		em = discord.Embed(name="User Info",
						   description= f"Information on: {user}",
						   color=choice(color_list))
		em.add_field(name='User ID', value=user.id, inline=True)
		if isinstance(user, discord.Member):
			voice_state = None if not user.voice else user.voice.channel
			em.add_field(name='Nickname', value=user.nick, inline=True)
			em.add_field(name='Status', value=user.status, inline=True)
			em.add_field(name='In Voice', value=voice_state, inline=True)
			em.add_field(name='Activity', value=user.activity, inline=True)
			em.add_field(name='Highest Role', value=role, inline=True)
		em.add_field(name='Account Created', value=user.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
		if isinstance(user, discord.Member):
			em.add_field(name='Join Date', value=user.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
		em.set_thumbnail(url=user.avatar_url)
		em.set_author(name=user, icon_url=self.azami.user.avatar_url)
		em.set_footer(text=f"Requested by {ctx.message.author.name} - Today at: " + (
							  time.strftime("%I:%M %p")))
		await ctx.send(embed=em)



def setup(azami):
	azami.add_cog(Server(azami))