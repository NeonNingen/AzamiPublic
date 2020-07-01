import discord, sys, io
from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument
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

	class Slapper(commands.Converter):
		async def convert(self, ctx, argument):
			to_slap = choice(ctx.guild.members)
			return f'{ctx.author} slapped {to_slap} because *{argument}*'

	@commands.command(description="It's your fault!")
	async def blame(self, ctx, *, reason: Slapper):
		await ctx.send(reason)

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
		with open('cogs/responses_fun.txt', 'r') as f:
			responses = f.read().splitlines()
			# When rehauling use folders for each cog
		await ctx.send(f"Questions: {question}\nAnswer: {choice(responses)}")

	@commands.command(description='azami -> AZAMI',
					  usage='Basically capitalizes anything you say')
	async def up(self, ctx, *, content: to_upper):
		await ctx.send(content)

	@commands.command(description='Bang and the dirt is gone',
					  usage='You can suicide, shoot others or shoot Azami!')
	async def shoot(self, ctx, *members: discord.Member):
		if not members: # Built in error check
			await ctx.send("You gotta give me someone to shoot!")
			return
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

		def check(c):
			return c.author == ctx.author and c.content.lower() in ['r', 'p', 's', 'q']

		while True:
			await ctx.send(f'Wins: {wins}, Losses: {losses}, Ties: {ties}', delete_after=5)
			choiceMessage = await ctx.send("What do you choose (r)ock, (p)aper, (s)cissors or (q)uit")
			try:
				inputChoice = await azami.wait_for('message', check=check, timeout=20)
			except:
				await ctx.send('You took too long to respond.')
				return
			inputChoice = inputChoice.content
			choiceMessage.delete()

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



	@blame.error
	async def blame_error(self, ctx, error):
		if isinstance(error, MissingRequiredArgument):
			await ctx.send("Requires a user to blame")

	@slap.error 
	async def slap_error(self, ctx, error):
		if isinstance(error, MissingRequiredArgument):
			await ctx.send("Requires a user to hit")

	@_8ball.error
	async def ball8_error(self, ctx, error):
		if isinstance(error, MissingRequiredArgument):
			await ctx.send("Please write a question for me to respond to")

	@up.error
	async def up_error(self, ctx, error):
		if isinstance(error, MissingRequiredArgument):
			await ctx.send("Please give me a word or sentence")

	@say.error
	async def say_error(self, ctx, error):
		if isinstance(error, MissingRequiredArgument):
			await ctx.send("Please give me a word or sentence")
	

def setup(azami):
	azami.add_cog(Fun(azami))
