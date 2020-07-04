import discord, sys, io
from discord.ext import commands
from random import choice, randint
from asyncio import sleep
sys.path.insert(1, '../')
import randomimg

# This cog is also a mess xD

def to_upper(argument):
	return argument.upper()

class Fun(commands.Cog):

	def __init__(self, azami):
		self.azami = azami

	@commands.command(description="It's your fault!")
	async def blame(self, ctx, *, reason):
		await ctx.send(f'{ctx.author} slapped {choice(ctx.guild.members)} because *{reason}*')

	@commands.command(description='This is gonna hurt!')
	async def slap(self, ctx, user):
		embed = discord.Embed(
			title = "That hurts!",
			description = f"{ctx.author.mention} slapped {user}",
			colour = discord.Color.dark_red())
		embed.set_image(url = randomimg.slap())
		await ctx.send(embed=embed)

	@commands.command(name='8 or 8ball', aliases=['8ball', '8'], 
					  description='What answers do you seek?',
					  usage='Have your questions answered!')
	async def _8ball(self, ctx, *, question):
		responses = ["It is certain.",
				"It is decidedly so.",
				"Without a doubt.",
				"Yes - definitely.",
				"You may rely on it.",
				"As I see it, yes.",
				"Most likely.",
				"Outlook good.",
				"Yes.",
				"Signs point to yes.",
				"Reply hazy, try again.",
				"Ask again later.",
				"Better not tell you now.",
				"Cannot predict now.",
				"Concentrate and ask again.",
				"Don't count on it.",
				"My reply is no.",
				"My sources say no.",
				"Outlook not so good.",
				"Very doubtful"
			    ]
		await ctx.send(f"Questions: {question}\nAnswer: {choice(responses)}")

	@commands.command(description='azami -> AZAMI',
					  usage='Basically capitalizes anything you say')
	async def up(self, ctx, *, content: to_upper):
		await ctx.send(content)

	@commands.command(description='Bang and the dirt is gone',
					  usage='You can suicide, shoot others or shoot Azami!')
	async def shoot(self, ctx, *members: discord.Member):
		for member in members:
			if member == self.azami.user:
				embed = discord.Embed(
					title = "Dodged it!",
					description = f"You attempted to shoot me {ctx.author.mention}, but I dodged it!",
					colour = discord.Color.green())
				embed.set_image(url = randomimg.shoot(1))
				await ctx.send(embed=embed)
			elif member == ctx.author:
				embed = discord.Embed(
					title = "You died! Better luck next time!",
					description = f"{ctx.author.name} committed suicide!",
					colour = discord.Color.red())
				embed.set_image(url = randomimg.shoot(2))
				await ctx.send(embed=embed)
			else:
				embed = discord.Embed(
					title = "It's a hit!",
					description = f"{member.name} was shot dead by the mighty {ctx.author.name}",
					colour = discord.Color.gold())
				embed.set_image(url = randomimg.shoot(3))
				await ctx.send(embed=embed)

	@commands.command(description='And your next line is!')
	async def say(self, ctx, *, content):
		await ctx.send(content)

	@commands.command(description="Let's play a game of Jan Ken Pon!",
					  aliases=['rockpaperscissors', 'rock'])
	async def rps(self, ctx):
		if ctx.author.id in rpsUsers:
			await ctx.send('Starting a new game', delete_after=5)
			rpsUser = rpsUsers[ctx.author.id]
			try:
				channel = azami.get_channel(rpsUser["channel"])
				msg1 = await channel.fetch_message(rpsUser["message1"])
				await msg1.delete()
				msg2 = await channel.fetch_message(rpsUser["message2"])
				await msg2.delete()
			except:
				#bit of a lazy way but does that really matter 
				pass
		
		#just want to put it out there that a dict is faster than a hashtable and that a hashtable is just a way to use a dict so go sugma
		choices = {'r' : 
						{"name" : "Rock",
						"compImage" : "https://technabob.com/blog/wp-content/uploads/2018/07/ksts_st_rock_mood_light_colors.gif", 
						"userImage" : "https://media.giphy.com/media/26gsdS1KCyxwTl6IU/giphy.gif", 
						"beats" : "s",
						"message" : "You threw out a rock",
						"colour" : discord.Color.greyple()},
					'p' : 
						{"name" : "Paper",
						"compImage" : "https://share.gifyoutube.com/yEMl0X.gif", 
						"userImage" : "https://media.giphy.com/media/l3q2RoEgmvxXIvA5i/giphy.gif", 
						"beats" : "r",
						"message" : "You hit me with paper",
						"colour" : discord.Color.teal()},
					's' : 
						{"name" : "Scissors",
						"compImage" : "https://66.media.tumblr.com/2037d7aa49c718d3229c14eddade2837/tumblr_ov7tlr0UzF1vz54q7o3_500.gifv", 
						"userImage" : "https://media1.giphy.com/media/jcBj1VbbrXgJy/source.gif", 
						"beats" : "p",
						"message" : "You slashed out some scissors",
						"colour" : discord.Color.red()}
					}

		hello_em = discord.Embed(title=f"Hello {ctx.message.author.name}",
								 description="Let's play Rock, paper, scissors!",
								 color=discord.Color.green())
		hello_em.set_image(url="https://media1.giphy.com/media/xUOwFX9O1080yxFDk4/source.gif")
		hello_em.set_thumbnail(url=ctx.message.author.avatar_url)
		hello_em.set_footer(text="Your opponent is me!",
							   icon_url=azami.user.avatar_url)
		msg = await ctx.send(embed=hello_em)


		inputChoice, wins, losses, ties = '', 0, 0, 0

		def check(r, c):
			return c.author == ctx.author and c.content.lower() in ['r', 'p', 's', 'q'] and msg.id == rpsUsers[ctx.author.id]['message1']
		
		#because of bad while loop, it's sort of hard to 'cancel' the wait_for, even if you delete the message or use reactions instead it will still respond once so no point - so I made the timeout not send a message
		while True:
			await ctx.send(f'Wins: {wins}, Losses: {losses}, Ties: {ties}', delete_after=5)
			choiceMessage = await ctx.send("What do you choose (r)ock, (p)aper, (s)cissors or (q)uit")
			try:
				inputChoice = await azami.wait_for('message', check=check, timeout=20)
			except:
				return
			rpsUsers[ctx.author.id] = {"channel" : ctx.channel.id, "message1" : msg.id, "message2" : choiceMessage.id}
			inputChoice = inputChoice.content
			choiceMessage.delete()
			inputMessage.delete()

			if inputChoice == 'q':
				await ctx.send("See you next time")
				return

			userChoice = choices[inputChoice.lower()]
			userEmbed = discord.Embed(title=userChoice["message"], 
									  description=f'{userChoice["name"]} against...', 
									  color=userChoice["colour"])
			userEmbed.set_image(url=userChoice["userImage"])
			userEmbed.set_thumbnail(url=ctx.message.author.avatar_url)
			await msg.edit(embed=userEmbed)

			randrps = choice(['r', 'p', 's'])
			compChoice = choices[randrps]
			compEmbed = discord.Embed(title=f'{compChoice["name"]}!', 
									  color=compChoice["colour"])
			compEmbed.set_image(url=compChoice["compImage"])
			compEmbed.set_thumbnail(url=azami.user.avatar_url)

			await asyncio.sleep(3)
			await msg.edit(embed=compEmbed)

			await ctx.send("Please wait...", delete_after=4)

			if inputChoice == randrps:
				embed = discord.Embed(title="It's a tie...",
									 description="Prepare to lose next time!",
									 color=discord.Color.purple())
				embed.set_image(url="https://i.makeagif.com/media/2-03-2016/2VqsWK.gif")
				embed.set_thumbnail(url=ctx.message.author.avatar_url)
				ties += 1

			elif userChoice["beats"] == randrps:
				embed = discord.Embed(title="Congrats you win!",
									 description="I'll get you next time!",
									 color=discord.Color.gold())
				embed.set_image(url="https://media.giphy.com/media/l0HlMWVJqvf86klnq/giphy.gif")
				embed.set_thumbnail(url=ctx.message.author.avatar_url)
				wins += 1

			else:
				embed = discord.Embed(title="Better luck next time!",
									 description="Ha! You lost!",
									 color=discord.Color.dark_red())
				embed.set_image(url="https://media.giphy.com/media/5MtOIdkHhxPFu/giphy.gif")
				embed.set_thumbnail(url=azami.user.avatar_url)
				losses += 1
			
			await asyncio.sleep(4)
			await msg.edit(embed=embed)
			

def setup(azami):
	azami.add_cog(Fun(azami))
	
	global rpsUsers
	rpsUsers = {}